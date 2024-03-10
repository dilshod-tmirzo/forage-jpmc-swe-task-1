import unittest
from typing import Any

from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):

        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
            # {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453','top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            ave_price = getDataPoint(quote)
            message = "First value and second value are equal !"
            self.assertEqual(ave_price[3], (quote['top_ask']['price'] + quote['top_bid']['price']) / 2, message)

    def test_getDataPoint_avePriceFail(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """

        for quote in quotes:
            ave_price = getDataPoint(quote)
            message = "First value and second value are not equal"
            self.assertNotEqual(ave_price[3], (quote['top_ask']['price'] + quote['top_bid']['price']) / 3, message)

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_whenSuccess(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        ave_price1 = (quotes[0]['top_ask']['price'] + quotes[0]['top_bid']['price']) / 2
        ave_price2 = (quotes[1]['top_ask']['price'] + quotes[1]['top_bid']['price']) / 2
        message = "First value and second value are not equal"
        self.assertGreater(getRatio(ave_price1, ave_price2), 1, message)


if __name__ == '__main__':
    unittest.main()
