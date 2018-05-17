#coding=utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from borrowertipspage import BorrowTipPage


class BorrowTipsTest(unittest.TestCase):
    def setUp(self):
        self.dr = my_driver()
        self.borrow_p = BorrowTipPage(self.dr)
        self.borrow_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.borrow_p.get_content()
        self.assertIn("网络借贷中介平台借款人提示", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()