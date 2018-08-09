#! /usr/bin/env python
# coding: utf-8
from zeep import Client as ZClient

class Currency():
    def __init__(self, unit="EUR"):
        client = ZClient("https://services.nbg.gov.ge/Rates/Service.asmx?wsdl")
        self.unit = unit
        self._data = client.service.GetLastRates(unit)[0]

    def get_currency(self):
        return self._data["Rate"]

    def get_description(self):
        return self._data["Name"]

    def get_change(self):
        return self._data["Diff"]

    def get_date(self):
        return self._data["Date"]

    def get_all(self):
        return self._data
