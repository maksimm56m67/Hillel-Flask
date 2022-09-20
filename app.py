from flask import Flask, request

from utils import get_currency_exchange_rate

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p><b>Hello, World!</b></p>"


@app.route("/rates", methods=['GET'])
def get_rates():
    currency_a = request.args.get('currency_a', default='UAH')
    currency_b = request.args.get('currency_b', default='USD')
    currency_date = request.args.get('currency_date', default='01.12.2014')
    curency_curse = request.args.get('curency_curse', default='НБУ')
    result = get_currency_exchange_rate(currency_a, currency_b, currency_date, curency_curse)
    return result
