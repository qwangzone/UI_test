import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from lendertipspage import LenderTipsPage


class LenderTipsTest(unittest.TestCase):
    """出借人提示"""
    def setUp(self):
        self.dr = my_driver()
        self.dr.maximize_window()
        self.lendert_p = LenderTipsPage(self.dr)
        self.lendert_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.lendert_p.get_content()
        self.assertIn("网络借贷中介平台出借人提示", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()