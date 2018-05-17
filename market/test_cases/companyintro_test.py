#coding=utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from companyintropage import CompanyInfoPage


class CompanyIntroTest(unittest.TestCase):
    """公司简介"""
    def setUp(self):
        self.dr = my_driver()
        self.comintro_p = CompanyInfoPage(self.dr)
        self.comintro_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.comintro_p.get_content()
        self.assertIn("公司简介", content)
        self.assertIn("企业信息", content)
        self.assertIn("网站信息", content)
        self.assertIn("公司大事件", content)
        self.assertIn("办公环境", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()