"""
编写名为test_city_country()的方法
"""

import unittest
from city_functions import get_city_name

class CityTestCase(unittest.TestCase):
    """测试get_city_name"""
    def test_city_country(self):
        city_names = get_city_name('shenzhen','china')
        self.assertEqual(city_names,'Shenzhen, China')

    def test_city_country_populatioon(self):
        city_names = get_city_name('shenzhen','china','25,000,000')
        self.assertEqual(city_names,'Shenzhen, China - population 25,000,000')

if __name__ == '__main__':
    unittest.main()
