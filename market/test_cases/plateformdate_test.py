#coding:utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from plateformdatepage import PlateDatePage


class NetLoanTest(unittest.TestCase):
    """平台数据"""
    def setUp(self):
        self.dr = my_driver()
        self.platedate_p = PlateDatePage(self.dr)
        self.platedate_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.platedate_p.get_content()
        self.assertIn("Overview", content)
        self.assertIn("项目成交量", content)
        self.assertIn("风险数据", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()