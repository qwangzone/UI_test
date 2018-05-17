#coding:utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from productpage import ProductPage


class ProductTest(unittest.TestCase):
    """产品介绍"""
    def setUp(self):
        self.dr = my_driver()
        self.product_p = ProductPage(self.dr)
        self.product_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.product_p.get_content()
        self.assertIn("产品介绍", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()