#coding:utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from safetypage import SafetyPage


class SafeTyTest(unittest.TestCase):
    """安全保障"""
    def setUp(self):
        self.dr = my_driver()
        self.dr.maximize_window()
        self.safe_p = SafetyPage(self.dr)
        self.safe_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.safe_p.get_content()
        self.assertIn("安全保障", content)
        self.assertIn("法律护航有保障", content)
    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()