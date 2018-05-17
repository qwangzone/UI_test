#coding:utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from p2pknowledgepage import NetLoanKnowPage


class NetLoanTest(unittest.TestCase):
    """网贷知识"""
    def setUp(self):
        self.dr = my_driver()
        self.dr.maximize_window()
        self.p2p_p = NetLoanKnowPage(self.dr)
        self.p2p_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.p2p_p.get_content()
        self.assertIn("Net loan knowledge", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()