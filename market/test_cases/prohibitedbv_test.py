#coding:utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from prohibitedbvpage import ProhibitedbvPage


class ProhibiteTest(unittest.TestCase):
    """禁止性行为"""
    def setUp(self):
        self.dr = my_driver()
        self.prohibite_p = ProhibitedbvPage(self.dr)
        self.prohibite_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.prohibite_p.get_content()
        self.assertIn("Prohibited behavior", content)
        self.assertIn("网贷平台禁止性行为提示", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()