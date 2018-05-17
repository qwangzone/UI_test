#coding=utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from chargestandardpage import ChargingPage


class ChargeStandardTest(unittest.TestCase):
    """收费标准"""
    def setUp(self):
        self.dr = my_driver()
        self.dr.maximize_window()
        self.charge_p = ChargingPage(self.dr)
        self.charge_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.charge_p.get_content()
        self.assertIn("出借人收费标准", content)
    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()