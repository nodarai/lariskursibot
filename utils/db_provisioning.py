# coding: utf-8
import pandas as pd
from units import UNITS
from models import initialize_db, RefCurrency, Rate


db_session = initialize_db()


_xlsx_conf = {
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

def read_meta():
    currencies = UNITS.keys() # ['EUR', 'USD']
    print('reading names')
    names = pd.read_excel(
        'exratesyearsgeo.xlsx',
        skiprows=_xlsx_conf['rows']['names'],
        usecols='D,P',
        names=currencies,
        nrows=1,
        header=None
    )
    print('reading quantities')
    quantities = pd.read_excel(
        'exratesyearsgeo.xlsx',
        skiprows=_xlsx_conf['rows']['quantity'],
        usecols='D,P',
        names=currencies,
        nrows=1,
        header=None
    )
    print('reading codes')
    codes = pd.read_excel(
        'exratesyearsgeo.xlsx',
        skiprows=_xlsx_conf['rows']['code'],
        usecols='D,P',
        names=currencies,
        nrows=1,
        header=None
    )
    for c in currencies:
        rc = RefCurrency(
            name=names[c][0],
            quantity=quantities[c][0],
            code=codes[c][0]
        )
        db_session.add(rc)
    db_session.commit()


def read_data():
    columns = _xlsx_conf['columns'].keys() # ['date', 'EUR', 'USD']
    print('reading data')
    data = pd.read_excel(
        'exratesyearsgeo.xlsx',
        skiprows=_xlsx_conf['rows']['values'],
        usecols= ','.join(_xlsx_conf['columns'].values()),
        header=None,
        names=columns
    )
    print('starting data insertion')

    eur_id = db_session.query(RefCurrency).filter(RefCurrency.code == 'EUR').one().id
    usd_id = db_session.query(RefCurrency).filter(RefCurrency.code == 'USD').one().id

    for i,row in data.iterrows():
        if not pd.isna(row['EUR']):
            rate_eur = Rate(
                currency_id=eur_id,
                rate=row['EUR'],
                date=row['date'].to_pydatetime()
            )
            db_session.add(rate_eur)
        if not pd.isna(row['USD']):
            rate_usd = Rate(
                currency_id=usd_id,
                rate=row['USD'],
                date=row['date'].to_pydatetime()
            )
            db_session.add(rate_usd)

    print('commiting changes')
    db_session.commit()


# read_meta()
read_data()
