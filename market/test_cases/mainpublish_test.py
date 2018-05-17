import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from mainpublishpage import MainPublishPage


class MainPublishTest(unittest.TestCase):
    """主体披露"""
    def setUp(self):
        self.dr = my_driver()
        self.mainp_p = MainPublishPage(self.dr)
        self.mainp_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.mainp_p.get_content()
        self.assertIn("基本情况", content)
        self.assertIn("备案信息", content)
        self.assertIn("其他信息", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()