#coding:utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from operationalreportpage import OperRportPage


class OperationalReportTest(unittest.TestCase):
    """运营报告"""
    def setUp(self):
        self.dr = my_driver()
        self.opera_p = OperRportPage(self.dr)
        self.opera_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.opera_p.get_content()
        self.assertIn("阿朋贷2018三月份报告", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()