import unittest
from bmi_calculator import BMI
from parameterized import parameterized

class TestBMI(unittest.TestCase):
    
    @parameterized.expand([
        (1.6, 45, "underweight"),
        (1.80, 50, "underweight"),
        (1.6, 52, "normal weight"),
        (1.80, 70, "normal weight"),
        (1.50, 60, "slightly overweight"),
        (1.70, 80, "slightly overweight"),
        (1.6, 80, "overweight"),
        (1.70, 95, "overweight"),
        (1.6, 100, "clinically obese"),
        (1.70, 130, "clinically obese"),
    ])
    def test_bmi_results(self, height, weight, expected):
        bmi = BMI(height, weight)
        actual = bmi.calculate_bmi()
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
