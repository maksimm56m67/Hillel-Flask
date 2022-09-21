import requests

def get_currency_exchange_rate( currency_a: str, currency_b: str, currency_date:str, curency_curse:str):

    response = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={currency_date}')
    json = response.json()

    if response.status_code == 200:
        for i in range(len(json.get("exchangeRate"))):
            if json.get("exchangeRate")[i].get('baseCurrency') == currency_a and json.get("exchangeRate")[i].get('currency')  == currency_b:
                rate_buyNB = json.get("exchangeRate")[i].get('saleRateNB')
                rate_sellNB = json.get("exchangeRate")[i].get('purchaseRateNB')
                rate_buy = json.get("exchangeRate")[i].get('saleRate')
                rate_sell = json.get("exchangeRate")[i].get('purchaseRate')
                if curency_curse == 'НБУ':
                    return f'Курс НБУ на {currency_date} при конвертации {currency_a} в {currency_b} - курс {rate_buyNB} : {rate_sellNB}'
                else:
                    return f'Курс ПриватБанка на {currency_date} при конвертации {currency_a} в {currency_b} - для покупки {rate_buy} и для продажи {rate_sell}'
    return f"Ошибка api {response.status_code}: {json.get('errorDescription')}"




