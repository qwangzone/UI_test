#coding:utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from riskeducationpage import RiskEducationPage


class RiskEducationTest(unittest.TestCase):
    """风险教育"""
    def setUp(self):
        self.dr = my_driver()
        self.risked_p = RiskEducationPage(self.dr)
        self.risked_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.risked_p.get_content()
        self.assertIn("Risk education", content)
        self.assertIn("不可抗力风险", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()