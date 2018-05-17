#coding:utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from positionpage import PostionPage


class PositionTest(unittest.TestCase):
    """联系我们"""
    def setUp(self):
        self.dr = my_driver()
        self.posit_p = PostionPage(self.dr)
        self.posit_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.posit_p.get_content()
        self.assertIn("公司位置", content)
        self.assertIn("关注我们", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()