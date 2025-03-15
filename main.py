# -*- coding: utf-8 -*-
# Python

"""Copyright (c) Alexander Fedotov.
This source code is licensed under the license found in the
LICENSE file in the root directory of this source tree.
"""
from requests import get
from requests.exceptions import RequestException
import datetime


def get_price():
    try:
        response = get('https://hourlypricing.comed.com/api?type=5minutefeed&format=json')
        prices = response.json()
        price24 = sum(float(price['price']) for price in prices) / len(prices)
        lastprice = prices[-1]
        hourprice = sum(float(price['price']) for price in prices[-12:]) / 12
        return price24, hourprice, lastprice
    except RequestException:
        return


if __name__ == '__main__':
    print(get_price())