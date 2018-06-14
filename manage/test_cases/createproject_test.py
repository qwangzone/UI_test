#coding=utf-8
from selenium import webdriver
import unittest, os, sys, time
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(dir + "/pages")
import createprojectpage, loginpage
sys.path.append(dir + "/test_data/")
from get_data import GetData
from parameterized import parameterized


class CreateProTest(unittest.TestCase):
    '''创建标的'''
    @classmethod
    def setUpClass(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.implicitly_wait(10)
        # 后台建标需先登录，登录操作
        self.lgpg = loginpage.LoginPage(self.dr)
        self.lgpg.open()
        self.lgpg.login()
        # 引用后台新建标的page
        self.create_page = createprojectpage.CreateNew(self.dr)
        self.create_page.open()

    @parameterized.expand([('test_project_name', 'project_name', 'project_name_t'),
                           ('test_project_status', 'project_status', 'project_status'),
                           ('test_project_category', 'project_category', 'project_category_t'),
                           ('test_projectNewType', 'projectNewType', 'projectNewType_t'),
                           ('test_financingMaturity', 'financingMaturity', 'financingMaturity_t'),
                           ('test_corporeType', 'corporeType', 'corporeType_t'),
                           ('test_amount', 'amount', 'amount_t'),
                           ('test_minBidAmount', 'minBidAmount', 'minBidAmount_t'),
                           ('test_repaymentCalcType', 'repaymentCalcType', 'repaymentCalcType_t'),
                           ('test_interestRatePercent', 'interestRatePercent', 'interestRatePercent_t'),
                           ('test_displayIntere stRate', 'displayInterestRate', 'displayInterestRate_t'),
                           ('test_start_time', 'start_time', 'start_time_t'),
                           ('test_end_time', 'end_time', 'end_time_t'),
                           ('test_contractFullID', 'contractFullID', 'contractFullID_t'),
                           ('test_contractType', 'contractType', 'contractType_t'),
                           ('test_loanContract', 'loanContract', 'loanContract_t'),
                           ('test_address', 'address', 'address'),
                           ('test_unicode', 'unicode', 'unicode'),
                           ('test_bondManId', 'bondManId', 'bondManId'),
                           ('test_custRatingAAA', 'custRatingAAA', 'custRating_t_bool'),
                           ('test_userName', 'userName', 'userName_t'),
                           ('test_borrowerUserID', 'borrowerUserID', 'borrowerUserID'),
                           ('test_borrowerUserRealName', 'borrowerUserRealName', 'borrowerUserRealName'),
                           ('test_borrowerUserIDCard', 'borrowerUserIDCard', 'borrowerUserIDCard'),
                           ('test_borrowerPayType', 'borrowerPayType', 'borrowerPayType'),
                           ('test_isrealborrower', 'isrealborrower', 'isRealBorrower'),
                           ('test_realBorrowerName', 'realBorrowerName', 'realBorrowerName'),
                           ('test_realBorrowerIdCard', 'realBorrowerIdCard', 'realBorrowerIdCard'),
                           ('test_area', 'area', 'area'),
                           ('test_purpose', 'purpose', 'purpose_t'),
                           ('test_houseGuaranteeInfo', 'houseGuaranteeInfo', 'houseGuaranteeInfo_t'),
                           ('test_projectDescription', 'projectDescription', 'projectDescription_t'),
                           ('test_repaymentSource', 'repaymentSource', 'repaymentSource_t'),
                           ('test_signAddr', 'signAddr', 'signAddr_t'),
                           ])
    def test1_create_success(self, name, method, data):
        """标的新建成功"""
       # self.create_page.open()
        self.copy_p = self.create_page.createnewproject()
        success_msg = self.create_page.get_save_success_msg()
        print("method:" + self.copy_p.get_all_info(method))
        print("data:" + GetData[data].value)
        self.assertIn("项目保存成功", success_msg)
        self.assertEqual(self.copy_p.get_all_info(method), GetData[data].value)

    #     self.assertEqual(self.copy_p.get_project_status(), GetData.project_status)
    #     self.assertEqual(self.copy_p.get_project_category(), GetData.project_category_t)
    #     self.assertEqual(self.copy_p.get_projectNewType(), GetData.projectNewType_t)
    #     self.assertEqual(self.copy_p.get_financingMaturity(), GetData.financingMaturity_t)
    #     self.assertEqual(self.copy_p.get_corporeType(), GetData.corporeType_t)
    #     self.assertEqual(self.copy_p.get_amount(), GetData.amount_t)
    #     self.assertEqual(self.copy_p.get_minBidAmount(), GetData.minBidAmount_t)
    #     self.assertEqual(self.copy_p.get_repaymentCalcType(), GetData.repaymentCalcType_t)
    #     self.assertEqual(self.copy_p.get_interestRatePercent(), GetData.interestRatePercent_t)
    #     self.assertEqual(self.copy_p.get_displayInterestRate(), GetData.displayInterestRate_t)
    #     self.assertEqual(self.copy_p.get_start_time(), GetData.start_time_t)
    #     self.assertEqual(self.copy_p.get_end_time(), GetData.end_time_t)
    #     self.assertEqual(self.copy_p.get_contractFullID(), GetData.contractFullID_t)
    #     self.assertEqual(self.copy_p.get_contractType(), GetData.contractType_t)
    #     self.assertEqual(self.copy_p.get_loanContract(), GetData.loanContract_t)
    #     self.assertEqual(self.copy_p.get_address(), GetData.address)
    #     self.assertEqual(self.copy_p.get_unicode(), GetData.unicode)
    #     self.assertEqual(self.copy_p.get_bondManId(), GetData.bondManId)
    #     self.assertEqual(self.copy_p.get_custRatingAAA(), "true")
    #     self.assertEqual(self.copy_p.get_userName(), GetData.userName_t)
    #     self.assertEqual(self.copy_p.get_borrowerUserID(), GetData.borrowerUserID)
    #     self.assertEqual(self.copy_p.get_borrowerUserRealName(), GetData.borrowerUserRealName)
    #     self.assertEqual(self.copy_p.get_borrowerUserIDCard(), GetData.borrowerUserIDCard)
    #     self.assertEqual(self.copy_p.get_borrowerPayType(), GetData.borrowerPayType)
    #     self.assertEqual(self.copy_p.get_isrealborrower(), GetData.isRealBorrower)
    #     self.assertEqual(self.copy_p.get_realBorrowerName(), GetData.realBorrowerName)
    #     self.assertEqual(self.copy_p.get_realBorrowerIdCard(), GetData.realBorrowerIdCard)
    #     self.assertEqual(self.copy_p.get_area(), GetData.area)
    #     self.assertEqual(self.copy_p.get_purpose(), GetData.purpose_t)
    #     self.assertEqual(self.copy_p.get_houseGuaranteeInfo(), GetData.houseGuaranteeInfo_t)
    #     self.assertEqual(self.copy_p.get_projectDescription(), GetData.projectDescription_t)
    #     self.assertEqual(self.copy_p.get_repaymentSource(), GetData.repaymentSource_t)
    #     self.assertEqual(self.copy_p.get_signAddr(), GetData.signAddr_t)
    #
    @parameterized.expand([("借款金额空", "借款金额 必须填写", "0"),
                         ("最小认购金额空", "最小认购金额 必须填写", "1"),
                         ("出借方年化利率空", "出借方年化利率 必须填写", "2"),
                         ("允许投标起始时间空", "允许投标起始时间 必须填写", "3"),
                         ("认购截止时间空", "认购截止时间 必须填写", "4"),
                         ("线上合同编号空", "线上合同编号 必须填写", "5"),
                         ("线下借款合同编号空", "线下借款合同编号 必须填写", "6"),
                         ("借款人用户ID空", "借款人用户ID 必须填写", "7"),
                         ("资金用途空", "资金用途 必须填写", "8")])
    def test2_create_required_para(self, name, assert_text, error_index):
        """必填项为空测试"""
        self.create_page.open()
        self.create_page.createprojectwrong()
        #time.sleep(3)
        self.create_page.alert_text()
        self.assertIn(assert_text, self.create_page.get_error_text(int(error_index)))
        # self.assertIn("还款来源必须填写", self.create_page.alert_text())
        # self.assertIn("借款金额 必须填写",self.create_page.get_error_text(0))
        # self.assertIn("最小认购金额 必须填写", self.create_page.get_error_text(1))
        # self.assertIn("出借方年化利率 必须填写", self.create_page.get_error_text(2))
        # self.assertIn("允许投标起始时间 必须填写", self.create_page.get_error_text(3))
        # self.assertIn("认购截止时间 必须填写", self.create_page.get_error_text(4))
        # self.assertIn("线上合同编号 必须填写", self.create_page.get_error_text(5))
        # self.assertIn("线下借款合同编号 必须填写", self.create_page.get_error_text(6))
        # self.assertIn("借款人用户ID 必须填写", self.create_page.get_error_text(7))
        # self.assertIn("资金用途 必须填写", self.create_page.get_error_text(8))

    def test11_repay_source_null(self):
        """还款来源为空"""
        self.create_page.open()
        self.create_page.createprojectwrong()
        self.assertIn("还款来源必须填写", self.create_page.alert_text())

    def test3_proname_wrong(self):
        """项目标题长度超限"""
        #self.create_page.open()
        self.create_page.createnewproject(project_name="1111111111111111")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("项目名称 的长度不能多于 15 个字", error_text)

    def test4_loanterm_not_num(self):
        """借款期限不为数字"""
        #self.create_page.open()
        self.create_page.createnewproject(financingMaturity="qq")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("借款期限 必须为数字", error_text)

    def test5_loanterm_wrong(self):
        """借款期限非法"""
        #self.create_page.open()
        self.create_page.createnewproject(financingMaturity="100")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("必须在0.1到48之间", error_text)

    def test6_loanamount_not_num(self):
        """借款金额不为数字"""
        #self.create_page.open()
        self.create_page.createnewproject(amount="qq")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("借款金额 必须为数字", error_text)

    def test7_loanamount_wrong(self):
        """借款金额非法"""
        #self.create_page.open()
        self.create_page.createnewproject(amount="100000000000")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("借款金额 必须在0到10000000000之间", error_text)

    def test8_minBidAmount_not_num(self):
        """最小认购金额不为数字"""
        #self.create_page.open()
        self.create_page.createnewproject(minBidAmount="qq")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("最小认购金额 必须为数字", error_text)

    def test9_minBidAmount_wrong(self):
        """最小认购金额非法"""
        #self.create_page.open()
        self.create_page.createnewproject(minBidAmount="100000000000")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("最小认购金额 必须在0到10000000000之间", error_text)

    def test10_interestRatePercent_not_num(self):
        """出借方年化利率不为数字"""
        #self.create_page.open()
        self.create_page.createnewproject(interestRatePercent="qq")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("出借方年化利率 必须为数字", error_text)

    def test11_interestRatePercent_wrong(self):
        """出借方年化利率非法"""
        #self.create_page.open()
        self.create_page.createnewproject(interestRatePercent="100")
        error_text = self.create_page.get_error_text(0)
        self.assertIn("出借方年化利率 必须在1到24之间", error_text)

    def test12_contractFullID_wrong(self):
        """线上合同编号长度超限"""
        #self.create_page.open()
        text = 'w'*101
        self.create_page.createnewproject(contractFullID=text)
        error_text = self.create_page.get_error_text(0)
        print(error_text)
        self.assertIn("线上合同编号 的长度不能多于 100 个字", error_text)

    def test13_loanContract_wrong(self):
        """线下合同编号长度超限"""
        #self.create_page.open()
        text = 'w' * 101
        self.create_page.createnewproject(loanContract=text)
        error_text = self.create_page.get_error_text(0)
        print(error_text)
        self.assertIn("线下借款合同编号 的长度不能多于 100 个字", error_text)

    @classmethod
    def tearDownClass(self):
        self.dr.quit()
        #print("end")


if __name__ == '__main__':
    unittest.main()
    # suit = unittest.TestSuite()
    # suit.addTest(CreateProTest('test_repay_source_null'))
    # runner = unittest.TextTestRunner()
    # runner.run(suit)
