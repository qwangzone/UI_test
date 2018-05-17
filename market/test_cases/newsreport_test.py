import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from newsreportpage import NewsReportPage


class NewsReportTest(unittest.TestCase):
    """新闻资讯"""
    def setUp(self):
        self.dr = my_driver()
        self.newsr_p = NewsReportPage(self.dr)
        self.newsr_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.newsr_p.get_content()
        self.assertIn("News report", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()