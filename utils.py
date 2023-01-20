import json
import requests
from config import keys


class ExchangeException(Exception):
    pass


class Exchange:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ExchangeException(f'Нельзя перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ExchangeException(f'Не смог обработать валюту {base}')

        try:
            amount = int(amount)
        except ValueError:
            raise ExchangeException(f'Не смог обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = float(json.loads(r.content)[keys[base]])
        return total_base * amount



# class ConvertionExeption(Exception):
#     pass
#
# import requests
# import json
# from config import keys
#
# class ConvertionExeption(Exception):
#     pass
#
#
#
# class CryptoConverter:
#     @staticmethod
#     def convert(quote: str, base: str, amount: str):
#        if quote == base:
#             raise ConvertionExeption(f'Невозможно перевести одинаковые валюты {base}.')
#        try:
#             quote_ticker = keys[quote]
#        except KeyError:
#             raise ConvertionExeption(f'Неудалось обработать валюту {quote}')
#
#        try:
#             base_ticker = keys[base]
#        except KeyError:
#             raise ConvertionExeption(f'Неудалось обработать валюту {base}')
#
#        try:
#             amount = float(amount)
#        except ValueError:
#             raise ConvertionExeption(f'Неудалось обработать количество {amount}')
#
#        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
#        total_base = json.loads(r.content)[keys[base]]
#
#        return total_base
