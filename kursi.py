#! /usr/bin/env python
# coding: utf-8
import requests
from telegram.ext import Updater
from telegram.ext import CommandHandler
from lxml import html
from datetime import date, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from utils.subscribers import Subscriber, Base
from functools import partial


from os import environ as env;TOKEN=env.get("KURSIBOT_TOKEN")
CURRENCIES = ("USD","EUR")
URL = "https://www.nbg.gov.ge/index.php"
DB_FILE = "kursi_subscribers.db"
QUERYSTRING = {"m":"582", "lng":"geo"}
PAYLOAD = {
        "action": "search",
        "date_end": "",
        "date_start":"",
        "item": "",
        "x":40,
        "y":8
    }
HEADERS = {
    'origin': "https://www.nbg.gov.ge",
    'upgrade-insecure-requests': "1",
    'content-type': "application/x-www-form-urlencoded",
    'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "https://www.nbg.gov.ge/index.php?m=582&lng=geo",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "en-US,en;q=0.9,fr;q=0.8",
    'cookie': "PHPSESSID=ailnfffso3pahubdtpfn86dk11",
    'cache-control': "no-cache"
    }

def get_date(num=0):
    return date.today() + timedelta(days=num)

def get_kursi(currency="EUR"):
    print("Getting kursi")
    yesterday_ = get_date(-1).strftime("%Y-%m-%d")
    tomorrow_ = get_date(1).strftime("%Y-%m-%d")
    PAYLOAD["item"] = currency
    PAYLOAD["date_start"] = yesterday_
    PAYLOAD["date_end"] = tomorrow_
    response = requests.request("POST", URL, data=PAYLOAD, headers=HEADERS, params=QUERYSTRING)
    root = html.fromstring(response.text)
    result = root.xpath("//div[@id = 'currency_id']/table/tr/td[4]")
    return result[-1].text_content().strip()

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="კეთილი იყოს თქვენი მობრძანება!")

def send_sorry(bot, update, error_message):
    msg = "დაფიქსირდა შეცდომა კურსის მოძიებისას.\n%s" % error_message
    bot.send_message(chat_id=update.message.chat_id, text=msg)

def get_usd(bot, update):
    print("Called usd command")
    try:
        msg = "დღეს 1 აშშ დოლარის ღირებულება შეადგენს %s ლარს" % get_kursi("USD")
    except Exception as ex:
        send_sorry(bot, update, repr(ex))
        print(repr(ex))
    else:
        bot.send_message(chat_id=update.message.chat_id, text=msg)

def get_eur(bot, update):
    print("Called eur command")
    try:
        msg = "დღეს 1 ევროს ღირებულება შეადგენს %s ლარს" % get_kursi("EUR")
    except Exception as ex:
        send_sorry(bot, update, repr(ex))
    else:
        bot.send_message(chat_id=update.message.chat_id, text=msg)

def initialize_db():
    engine = create_engine('sqlite:///subscribers.db')
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session

def subscribe(bot, update, db_session):
    chat_id = update.message.chat_id
    if db_session.query(Subscriber).filter(Subscriber.chat_id == chat_id).count():
        msg = "თქვენ უკვე გამოწერილი გაქვთ განახლებები."
    else:
        subscriber = Subscriber(chat_id=chat_id)
        db_session.add(subscriber)
        db_session.commit()
        msg = "თქვენ გამოიწერეთ ლარის კურსის განახლებები."
    bot.send_message(chat_id=chat_id, text=msg)

def unsubscribe(bot, update, db_session):
    chat_id = update.message.chat_id
    try:
        subscriber = db_session.query(Subscriber)\
            .filter(Subscriber.chat_id == chat_id).one()
    except NoResultFound:
        msg = "თქვენ არ გაქვთ გამოწერილი ლარის კურსის განახლებები."
    else:
        db_session.delete(subscriber)
        msg = "თქვენ გააუქმეთ ლარის კურსის განახლებების გამოწერა."
    finally:
        db_session.commit()
    bot.send_message(chat_id=chat_id, text=msg)

def main():
    db_session = initialize_db()
    subscribe_ses = partial(subscribe, db_session=db_session)
    unsubscribe_ses = partial(unsubscribe, db_session=db_session)

    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    # Add handler for start command
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    # Commands
    print("Adding handlers.")
    usd_handler = CommandHandler('usd', get_usd)
    dispatcher.add_handler(usd_handler)
    eur_handler = CommandHandler('eur', get_eur)
    dispatcher.add_handler(eur_handler)

    dispatcher.add_handler(CommandHandler('subscribe', subscribe_ses))
    dispatcher.add_handler(CommandHandler('unsubscribe', unsubscribe_ses))

    # Start infinit loop to respond to requests
    print("Starting polling")
    updater.start_polling()

if __name__=="__main__":
    main()
