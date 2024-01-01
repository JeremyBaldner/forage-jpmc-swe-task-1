import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36},
             'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109},
             'id': '0.109974697771',
             'stock': 'ABC'},

            {'top_ask': {'price': 121.68, 'size': 4},
             'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81},
             'id': '0.109974697771', 'stock': 'DEF'}
        ]
        # assert the get Data Point funtion works correctly
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'],
                                                   float(quote['top_bid']['price']),
                                                   float(quote['top_ask']['price']),
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2),
                             'The tuples do not match')

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36},
             'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109},
             'id': '0.109974697771',
             'stock': 'ABC'},

            {'top_ask': {'price': 121.68, 'size': 4},
             'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81},
             'id': '0.109974697771',
             'stock': 'DEF'}
        ]
        # assert the get Data Point funtion works correctly
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'],
                                                   float(quote['top_bid']['price']),
                                                   float(quote['top_ask']['price']),
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2),
                             'The tuples do not match')

    def test_getRatio_calculate(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36},
             'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109},
             'id': '0.109974697771',
             'stock': 'ABC'},

            {'top_ask': {'price': 121.68, 'size': 4},
             'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81},
             'id': '0.109974697771',
             'stock': 'DEF'}
        ]
        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
        # check the ratios are equal up to 3 decimal places
        self.assertAlmostEqual(getRatio(prices["ABC"], prices["DEF"]),
                               (prices['ABC'] / prices['DEF']), 3,
                               'Ratios are not equal')
        # check the ratio will not calculate a denominator of 0
        self.assertEqual(getRatio(prices["ABC"], 0), None, 'Function did not catch the denominator of 0')


if __name__ == '__main__':
    unittest.main()
