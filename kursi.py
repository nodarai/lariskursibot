#! /usr/bin/env python3
# coding: utf-8
from io import BytesIO
from os import environ as env
from functools import partial

import pandas as pd
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy.orm.exc import NoResultFound
from dotenv import load_dotenv, find_dotenv

from utils.models import (
    Subscriber,
    Rate,
    RefCurrency,
    initialize_db,
)
from utils.currency import Currency
from utils.units import UNITS
from utils.logger import logging


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

TOKEN = env.get("KURSIBOT_TOKEN")


async def get_kursi(update: Update, context: ContextTypes.DEFAULT_TYPE, unit="EUR"):
    currency = Currency(unit)
    data = currency.get_all()
    msg = "%s თარიღით %s შეადგენს %s ლარს " % \
          (data["Date"], data["Name"], data["Rate"])
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="""
    კეთილი იყოს თქვენი მობრძანება!
    შეგიძლიათ გამოიყენოთ შემდეგი ბრძანებები:
    /subscribe - დოლარის და ევროს კურსის განახლების გამოწერა. ყოველდღიურად მიიღებთ შეტყობინებას მომდევნო დღის კურსის შესატყობად.
    /unsubscribe - ზემოთ აღწერილი გამოწერის გაუქმება.
    /usd - ამერიკული დოლარის უახლესი კურსის გაგება.
    /eur - ევროს უახლესი კურსის გაგება.
    /plot - ლარის კურსის გრაფიკი.
    """)


async def send_sorry(update: Update, context: ContextTypes.DEFAULT_TYPE, error_message):
    msg = "დაფიქსირდა შეცდომა კურსის მოძიებისას.\n%s" % error_message
    await context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


async def subscribe(update: Update, context: ContextTypes.DEFAULT_TYPE, db_session):
    chat_id = update.effective_chat.id
    if db_session.query(Subscriber).filter(Subscriber.chat_id == chat_id).count():
        msg = "თქვენ უკვე გამოწერილი გაქვთ განახლებები."
    else:
        subscriber = Subscriber(chat_id=chat_id)
        db_session.add(subscriber)
        db_session.commit()
        msg = "თქვენ გამოიწერეთ ლარის კურსის განახლებები."
        logging.debug('User subscribed to rate updates')
    await context.bot.send_message(chat_id=chat_id, text=msg)


async def unsubscribe(update: Update, context: ContextTypes.DEFAULT_TYPE, db_session):
    chat_id = update.effective_chat.id
    try:
        subscriber = db_session.query(Subscriber)\
            .filter(Subscriber.chat_id == chat_id).one()
    except NoResultFound:
        msg = "თქვენ არ გაქვთ გამოწერილი ლარის კურსის განახლებები."
    else:
        db_session.delete(subscriber)
        logging.debug('User unsubscribed to rate updates')
        msg = "თქვენ გააუქმეთ ლარის კურსის განახლებების გამოწერა."
    finally:
        db_session.commit()
    await context.bot.send_message(chat_id=chat_id, text=msg)


async def inform_subscribers(db_session, application):
    currencies = ("USD", "EUR")
    datas = [Currency(c).get_all() for c in currencies]
    msgs = ["%s თარიღით %s შეადგენს %s ლარს \n\n" % \
            (data["Date"], data["Name"], data["Rate"])
            for data in datas]
    msg = "".join(msgs)
    subscribers = db_session.query(Subscriber).all()
    for subscriber in subscribers:
        logging.debug('Sending message to subscriber: %s' % subscriber.chat_id)
        await application.bot.send_message(chat_id=subscriber.chat_id, text=msg)


async def plot(update: Update, context: ContextTypes.DEFAULT_TYPE, db_session):
    logging.debug('Reading data')
    r2 = aliased(Rate)
    rates = db_session.query(Rate.date, Rate.rate, r2.rate)\
        .filter(Rate.currency_id == 1)\
        .join((r2, r2.date == Rate.date))\
        .filter(r2.currency_id == 2)\
        .order_by(Rate.date)

    df = pd.DataFrame(rates, columns=('day', 'EUR', 'USD'))\
        .set_index(keys='day', drop=True)

    img_buf = BytesIO()
    img_buf.name = 'plot.png'
    fig = df.plot.line().get_figure()
    fig.set_size_inches(20, 7)
    fig.savefig(img_buf, format='png')
    logging.debug("Chart ready. Sending it")
    img_buf.seek(0)
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img_buf)


def main():
    db_session = initialize_db()
    subscribe_ses = partial(subscribe, db_session=db_session)
    unsubscribe_ses = partial(unsubscribe, db_session=db_session)
    plot_fun = partial(plot, db_session=db_session)

    application = Application.builder().token(TOKEN).build()

    # Add handler for start command
    application.add_handler(CommandHandler('start', start))

    # Add handlers for currency commands
    for unit, commands in UNITS.items():
        get_unit = partial(get_kursi, unit=unit)
        for command in commands:
            application.add_handler(CommandHandler(command, get_unit))

    application.add_handler(CommandHandler('subscribe', subscribe_ses))
    application.add_handler(CommandHandler('unsubscribe', unsubscribe_ses))
    application.add_handler(CommandHandler('plot', plot_fun))

    logging.info('Starting polling...')
    application.run_polling()


if __name__ == "__main__":
    main()
