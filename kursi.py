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
from functools import partial
from utils.subscribers import Subscriber, Base
from utils.currency import Currency


from os import environ as env;TOKEN=env.get("KURSIBOT_TOKEN")
CURRENCIES = ("USD","EUR")

def get_kursi(unit="EUR"):
    currency = Currency(unit)
    return currency.get_currency()

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
