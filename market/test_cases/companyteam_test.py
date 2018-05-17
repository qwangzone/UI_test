#coding=utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from companyteampage import CompanyTeamPage


class CompanyTeamTest(unittest.TestCase):
    """高管团队"""
    def setUp(self):
        self.dr = my_driver()
        self.compt_p = CompanyTeamPage(self.dr)
        self.compt_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.compt_p.get_content()
        self.assertIn("高管团队", content)
        self.assertIn("员工信息", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()