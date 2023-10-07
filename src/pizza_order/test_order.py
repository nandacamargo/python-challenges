import unittest
from order import Order
from parameterized import parameterized

class TestOrder(unittest.TestCase):
    
    @parameterized.expand([
        ("L", "Y", "Y", 29),
        ("L", "Y", "N", 28),
        ("L", "N", "Y", 26),
        ("L", "N", "N", 25),
        ("M", "Y", "Y", 24),
        ("M", "Y", "N", 23),
        ("M", "N", "Y", 21),
        ("M", "N", "N", 20),
        ("S", "Y", "Y", 18),
        ("S", "Y", "N", 17),
        ("S", "N", "Y", 16),
        ("S", "N", "N", 15) 
    ])
    def test_valid_order(self, size, pepperoni, extra_cheese, expected):
        order = Order(size, pepperoni, extra_cheese)
        actual = order.calculate_bill()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
