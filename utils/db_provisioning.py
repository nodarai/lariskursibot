# coding: utf-8
import pandas as pd
from sqlalchemy import exists

from units import UNITS
from models import initialize_db, RefCurrency, Rate
from logger import logging


class CurrencyReader():
    """
    Reads metada and real data from an excel file and writes it to database.
    The excel file represents the historical data of the GEL exchange rate.
    The file can be downloaded at: https://www.nbg.gov.ge/index.php?m=582
    For the moment configuration takes in account only USD and EUR.

    Usage:
    currency_reader = CurrencyReader(excel_file)
    currency_reader.read_meta()
    currency_reader.read_data()
    """
    _XLSX_CONF = {
        'rows': {
            'names': 3,
            'quantity': 4,
            'code': 5,
            'values': 6,
        },
        'columns':  {
            'date': 'A',
            'EUR': 'D',
            'USD': 'P',
        }
    }

    def __init__(self, excel_file):
        self.excel_file = excel_file
        self.db_session = initialize_db()

    def read_meta(self):
        currencies = UNITS.keys() # ['EUR', 'USD']
        usecols = ','.join([self._XLSX_CONF['columns'][c] for c in currencies])
        logging.debug('reading names')
        names = pd.read_excel(
            self.excel_file,
            skiprows=self._XLSX_CONF['rows']['names'],
            usecols=usecols,
            names=currencies,
            nrows=1,
            header=None
        )
        logging.debug('reading quantities')
        quantities = pd.read_excel(
            self.excel_file,
            skiprows=self._XLSX_CONF['rows']['quantity'],
            usecols=usecols,
            names=currencies,
            nrows=1,
            header=None
        )
        logging.debug('reading codes')
        codes = pd.read_excel(
            self.excel_file,
            skiprows=self._XLSX_CONF['rows']['code'],
            usecols=usecols,
            names=currencies,
            nrows=1,
            header=None
        )
        for c in currencies:
            currency_exists = self.db_session.query(
                    exists().where(RefCurrency.code == codes[c][0])
                ).scalar()
            if not currency_exists:
                rc = RefCurrency(
                    name=names[c][0],
                    quantity=quantities[c][0],
                    code=codes[c][0]
                )
                self.db_session.add(rc)
        logging.debug('commiting changes')
        self.db_session.commit()


    def read_data(self):
        columns = self._XLSX_CONF['columns'].keys() # ['date', 'EUR', 'USD']
        logging.debug('reading data')
        data = pd.read_excel(
            self.excel_file,
            skiprows=self._XLSX_CONF['rows']['values'],
            usecols= ','.join(self._XLSX_CONF['columns'].values()),
            header=None,
            names=columns
        )
        logging.debug('starting data insertion')

        eur_id = self.db_session.query(RefCurrency).filter(RefCurrency.code == 'EUR').one().id
        usd_id = self.db_session.query(RefCurrency).filter(RefCurrency.code == 'USD').one().id

        for _, row in data.iterrows():
            if not pd.isna(row['EUR']):
                rate_exists = self.db_session.query(
                    exists().where(Rate.currency_id == eur_id)
                        .where(Rate.date == row['date'])
                ).scalar()
                if not rate_exists:
                    rate_eur = Rate(
                        currency_id=eur_id,
                        rate=row['EUR'],
                        date=row['date'].to_pydatetime()
                    )
                    self.db_session.add(rate_eur)
            if not pd.isna(row['USD']):
                rate_exists = self.db_session.query(
                    exists().where(Rate.currency_id == usd_id)
                        .where(Rate.date == row['date'])
                ).scalar()
                if not rate_exists:
                    rate_usd = Rate(
                        currency_id=usd_id,
                        rate=row['USD'],
                        date=row['date'].to_pydatetime()
                    )
                    self.db_session.add(rate_usd)

        logging.debug('commiting changes')
        self.db_session.commit()


if __name__ == '__main__':
    excel_file = 'exratesyearsgeo.xlsx'
    currency_reader = CurrencyReader(excel_file)
    currency_reader.read_meta()
    currency_reader.read_data()
    currency_reader.db_session.close()
