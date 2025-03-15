# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from requests import get
from requests.exceptions import RequestException
import datetime
import pytz


def get_price():
    try:
        response = get('https://hourlypricing.comed.com/api?type=5minutefeed&format=json')
        prices = response.json()
        price24 = sum(float(price['price']) for price in prices) / len(prices)
        seconds_UTC = int(int(prices[-1]['millisUTC'])/1000)
        dt_utc = datetime.datetime.fromtimestamp(seconds_UTC, tz=pytz.UTC)
        cst_tz = pytz.timezone('US/Central')
        lasttime = dt_utc.astimezone(cst_tz)
        # lasttime = datetime.datetime.strptime(prices[-1]['millisUTC'], '%Y-%m-%d %H:%M:%S')
        m1 = prices[-2]['price']
        m2 = prices[-3]['price']
        lastprice = prices[-1]['price']
        hourprice = sum(float(price['price']) for price in prices[-12:]) / 12
        return price24, hourprice, lastprice
    except RequestException:
        return


if __name__ == '__main__':
    # https://hourlypricing.comed.com/live-prices/five-minute-prices/
    print(get_price())