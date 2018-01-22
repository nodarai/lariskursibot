#! /usr/bin/env python
# coding: utf-8
from zeep import Client as ZClient

class Currency():
    def __init__(self, unit="EUR"):
        client = ZClient("http://nbg.gov.ge/currency.wsdl")
        self.unit = unit
        self._data = {
            "currency": client.service.GetCurrency(unit),
            "description": client.service.GetCurrencyDescription(unit),
            "change": client.service.GetCurrencyChange(unit),
            "date": client.service.GetDate()
        }
        
    def get_currency(self):
        return self._data["currency"]
        
    def get_description(self):
        return self._data["description"]
        
    def get_change(self):
        return self._data["change"]
        
    def get_date(self):
        return self._data["date"]
        
    def get_all(self):
        return self._data