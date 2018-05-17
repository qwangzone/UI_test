import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from lowspage import LawerPage


class LowsTest(unittest.TestCase):
    """法律法规"""
    def setUp(self):
        self.dr = my_driver()
        self.lows_p = LawerPage(self.dr)
        self.lows_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.lows_p.get_content()
        self.assertIn("法律法规", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()