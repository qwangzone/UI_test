#coding=utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from companyhonor import CompanyHrPage


class CompanyHonorTest(unittest.TestCase):
    """公司荣誉"""
    def setUp(self):
        self.dr = my_driver()
        self.comh_p = CompanyHrPage(self.dr)
        self.comh_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.comh_p.get_content()
        self.assertIn("荣誉证书", content)
        self.assertIn("数据接入", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()