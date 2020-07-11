from fuzzywuzzy import process
import requests


def getCompany(text):
    r = requests.get('https://api.iextrading.com/1.0/ref-data/symbols')
    stockList = r.json()
    return process.extractOne(text.strip(), stockList)

#@todo only us symbols
# print(getCompany('GOOG'))
print(getCompany('Hoa Sen Group'))
