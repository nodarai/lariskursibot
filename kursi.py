#! /usr/bin/env python3
# coding: utf-8
from telegram.ext import Updater
from telegram.ext import CommandHandler
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from functools import partial
from utils.subscribers import Subscriber, Base
from utils.currency import Currency
from utils.units import UNITS
from utils.thread_schedule import ThreadSchedule


from os import environ as env;TOKEN=env.get("KURSIBOT_TOKEN")
CURRENCIES = ("USD","EUR")

def get_kursi(bot, update, unit="EUR"):
    currency = Currency(unit)
    data = currency.get_all()
    msg = "%s თარიღით %s შეადგენს %s ლარს " % \
        (data["date"], data["description"], data["currency"])
    bot.send_message(chat_id=update.message.chat_id, text=msg)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="კეთილი იყოს თქვენი მობრძანება!")

def send_sorry(bot, update, error_message):
    msg = "დაფიქსირდა შეცდომა კურსის მოძიებისას.\n%s" % error_message
    bot.send_message(chat_id=update.message.chat_id, text=msg)

def initialize_db():
    engine = create_engine('sqlite:///subscribers.db',
                            connect_args={'check_same_thread': False})
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

def inform_subscribers(bot, db_session):
    currencies = ("USD", "EUR")
    datas = [Currency(c).get_all() for c in currencies]
    msgs = ["%s თარიღით %s შეადგენს %s ლარს \n\n" % \
            (data["date"], data["description"], data["currency"])
            for data in datas]
    msg = "".join(msgs)
    subscribers = db_session.query(Subscriber).all()
    for subscriber in subscribers:
        print(subscriber.chat_id)
        bot.send_message(chat_id=subscriber.chat_id, text=msg)

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
    for unit, commands in UNITS.items():
        get_unit = partial(get_kursi, unit=unit)
        for command in commands:
            dispatcher.add_handler(CommandHandler(command, get_unit))

    dispatcher.add_handler(CommandHandler('subscribe', subscribe_ses))
    dispatcher.add_handler(CommandHandler('unsubscribe', unsubscribe_ses))
    # Create separete thread to run daily tasks
    th = ThreadSchedule(partial(inform_subscribers, updater.bot, db_session))
    th.start()
    # Start infinit loop to respond to requests
    print("Starting polling")
    updater.start_polling()

if __name__=="__main__":
    main()
