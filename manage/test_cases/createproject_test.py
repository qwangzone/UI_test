#coding=utf-8
from selenium import webdriver
import unittest, os, sys, time
from datetime import datetime, timedelta

dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
import createprojectpage, loginpage


class CreateProTest(unittest.TestCase):
    '''创建标的测试'''

    def setUp(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.implicitly_wait(10)
        # 后台建标需先登录，登录操作
        self.lgpg = loginpage.LoginPage(self.dr)
        self.lgpg.open()
        self.lgpg.login()
        # 引用后台新建标的page
        self.create_page = createprojectpage.CreateNew(self.dr)

    def test1_create_success(self):
        """标的新建成功"""
        self.create_page.open()
        self.create_page.createnewproject()
        success_msg = self.create_page.get_save_success_msg()
        self.assertIn("项目保存成功", success_msg)

    def test2_create_required_para(self):
        """必填项为空测试"""
        self.create_page.open()
        self.create_page.createprojectwrong()
        self.assertIn("还款来源必须填写", self.create_page.alert_text())
        self.assertIn("借款金额 必须填写",self.create_page.get_error_text(0))
        self.assertIn("最小认购金额 必须填写", self.create_page.get_error_text(1))
        self.assertIn("出借方年化利率 必须填写", self.create_page.get_error_text(2))
        self.assertIn("允许投标起始时间 必须填写", self.create_page.get_error_text(3))
        self.assertIn("认购截止时间 必须填写", self.create_page.get_error_text(4))
        self.assertIn("线上合同编号 必须填写", self.create_page.get_error_text(5))
        self.assertIn("线下借款合同编号 必须填写", self.create_page.get_error_text(6))
        self.assertIn("借款人用户ID 必须填写", self.create_page.get_error_text(7))
        self.assertIn("资金用途 必须填写", self.create_page.get_error_text(8))

    def test3_proname_wrong(self):
        """项目标题长度超限"""
        self.create_page.open()
        self.create_page.createnewproject(project_name="1111111111111111")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("项目名称 的长度不能多于 15 个字", error_text)

    def test4_loanterm_not_num(self):
        """借款期限不为数字"""
        self.create_page.open()
        self.create_page.createnewproject(financingMaturity="qq")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("借款期限 必须为数字", error_text)

    def test5_loanterm_wrong(self):
        """借款期限非法"""
        self.create_page.open()
        self.create_page.createnewproject(financingMaturity="100")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("必须在0.1到48之间", error_text)

    def test6_loanamount_not_num(self):
        """借款金额不为数字"""
        self.create_page.open()
        self.create_page.createnewproject(amount="qq")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("借款金额 必须为数字", error_text)

    def test7_loanamount_wrong(self):
        """借款金额非法"""
        self.create_page.open()
        self.create_page.createnewproject(amount="100000000000")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("借款金额 必须在0到10000000000之间", error_text)

    def test8_minBidAmount_not_num(self):
        """最小认购金额不为数字"""
        self.create_page.open()
        self.create_page.createnewproject(minBidAmount="qq")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("最小认购金额 必须为数字", error_text)

    def test9_minBidAmount_wrong(self):
        """最小认购金额非法"""
        self.create_page.open()
        self.create_page.createnewproject(minBidAmount="100000000000")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("最小认购金额 必须在0到10000000000之间", error_text)

    def test10_interestRatePercent_not_num(self):
        """出借方年化利率不为数字"""
        self.create_page.open()
        self.create_page.createnewproject(interestRatePercent="qq")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("出借方年化利率 必须为数字", error_text)

    def test11_interestRatePercent_wrong(self):
        """出借方年化利率非法"""
        self.create_page.open()
        self.create_page.createnewproject(interestRatePercent="100")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("出借方年化利率 必须在1到24之间", error_text)

    def test12_contractFullID_wrong(self):
        """线上合同编号长度超限"""
        self.create_page.open()
        text = 'w'*101
        self.create_page.createnewproject(contractFullID=text)
        error_text = self.create_page.get_error_text(0)
        print(error_text)
        self.assertIn("线上合同编号 的长度不能多于 100 个字", error_text)

    def test13_loanContract_wrong(self):
        """线下合同编号长度超限"""
        self.create_page.open()
        text = 'w' * 101
        self.create_page.createnewproject(loanContract=text)
        error_text = self.create_page.get_error_text(0)
        print(error_text)
        self.assertIn("线下借款合同编号 的长度不能多于 100 个字", error_text)


    def tearDown(self):
        self.dr.quit()
        # print("end")


if __name__ == '__main__':
    unittest.main()
    # suit = unittest.TestSuite()
    # suit.addTest(CreateProTest('test1_create_success'))
    # runner = unittest.TextTestRunner()
    # runner.run(suit)
