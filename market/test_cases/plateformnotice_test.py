#coding:utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from plateformnoticepage import PlateNoticePage


class PlateNoticeTest(unittest.TestCase):
    """平台公告"""
    def setUp(self):
        self.dr = my_driver()
        self.plate_p = PlateNoticePage(self.dr)
        self.plate_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.plate_p.get_content()
        self.assertIn("Platform notice", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()