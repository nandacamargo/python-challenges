import unittest
from leap_year import leap_year

class TestLeapYear(unittest.TestCase):

    '''This test validades the function for leap years'''
    def test_leap_year(self):

        with open("leap_years.txt", "r") as f:
            lines = f.readlines()

            for line in lines:
                year = int(line.strip())
                answer = leap_year(year)

                self.assertTrue(answer)


    '''This test validades the function for non leap years'''
    def test_non_leap_year(self):                

        with open("non_leap_years.txt", "r") as f:
            lines = f.readlines()

            for line in lines:
                year = int(line.strip())
                answer = leap_year(year)

                self.assertFalse(answer)
        

if __name__ == '__main__':
    unittest.main()
