from forex_python.converter import CurrencyRates

cr = CurrencyRates()

def currency_converter(amount, from_currency, to_currency):
    return cr.convert( from_currency, to_currency,amount)

print(currency_converter(3.63, 'USD', 'INR'))
