#coding:utf-8
import unittest
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/driver")
# from market.driver.driver import my_driver
# from market.pages.borrowertipspage import BorrowTipPage
from driver import my_driver
from riskmanagementpage import RiskManegePage


class riskmanageTest(unittest.TestCase):
    """风险管理"""
    def setUp(self):
        self.dr = my_driver()
        self.riskma_p = RiskManegePage(self.dr)
        self.riskma_p.open()

    def test1_content(self):
        """页面内容显示"""
        content = self.riskma_p.get_content()
        self.assertIn("风险管理框架", content)
        self.assertIn("风险预警流程", content)

    def tearDown(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()