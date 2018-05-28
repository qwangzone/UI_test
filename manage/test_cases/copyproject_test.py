# coding=utf-8
from selenium import webdriver
import unittest, os, sys
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/test_data/")
import copyprojectpage, loginpage, createprojectpage
from get_data import GetData




class CopyProTest(unittest.TestCase):
    '''测试复制标的'''

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
        self.create_page.open()
        self.copy_p = self.create_page.createnewproject()

    def test_copypro(self):
        self.copy_p.save_proinfo()
        success_msg = self.copy_p.get_save_success_msg()
        self.assertIn("项目保存成功", success_msg)
        self.assertEqual(self.copy_p.get_project_name(), "复制标的")
        self.assertEqual(self.copy_p.get_project_status(), GetData.project_status)
        self.assertEqual(self.copy_p.get_project_category(), GetData.project_category_t)
        self.assertEqual(self.copy_p.get_projectNewType(), GetData.projectNewType_t)
        self.assertEqual(self.copy_p.get_financingMaturity(), GetData.financingMaturity_t)
        self.assertEqual(self.copy_p.get_corporeType(), GetData.corporeType_t)
        self.assertEqual(self.copy_p.get_amount(), GetData.amount_t)
        self.assertEqual(self.copy_p.get_minBidAmount(), GetData.minBidAmount_t)
        self.assertEqual(self.copy_p.get_repaymentCalcType(), GetData.repaymentCalcType_t)
        self.assertEqual(self.copy_p.get_interestRatePercent(), GetData.interestRatePercent_t)
        self.assertEqual(self.copy_p.get_displayInterestRate(), GetData.displayInterestRate_t)
        self.assertEqual(self.copy_p.get_start_time(), GetData.start_time_t)
        self.assertEqual(self.copy_p.get_end_time(), GetData.end_time_t)
        self.assertEqual(self.copy_p.get_contractFullID(), GetData.contractFullID_t)
        self.assertEqual(self.copy_p.get_contractType(), GetData.contractType_t)
        self.assertEqual(self.copy_p.get_loanContract(), GetData.loanContract_t)
        self.assertEqual(self.copy_p.get_address(), GetData.address)
        self.assertEqual(self.copy_p.get_unicode(), GetData.unicode)
        self.assertEqual(self.copy_p.get_bondManId(), GetData.bondManId)
        self.assertEqual(self.copy_p.get_userName(), GetData.userName_t)
        self.assertEqual(self.copy_p.get_borrowerUserID(), GetData.borrowerUserID)
        self.assertEqual(self.copy_p.get_borrowerUserRealName(), GetData.borrowerUserRealName)
        self.assertEqual(self.copy_p.get_borrowerUserIDCard(), GetData.borrowerUserIDCard)
        self.assertEqual(self.copy_p.get_borrowerPayType(), GetData.borrowerPayType)
        self.assertEqual(self.copy_p.get_isrealborrower(), GetData.isRealBorrower)
        self.assertEqual(self.copy_p.get_realBorrowerName(), GetData.realBorrowerName)
        self.assertEqual(self.copy_p.get_realBorrowerIdCard(), GetData.realBorrowerIdCard)
        self.assertEqual(self.copy_p.get_area(), GetData.area)
        self.assertEqual(self.copy_p.get_purpose(), GetData.purpose_t)
        self.assertEqual(self.copy_p.get_houseGuaranteeInfo(), GetData.houseGuaranteeInfo_t)
        self.assertEqual(self.copy_p.get_projectDescription(), GetData.projectDescription_t)
        self.assertEqual(self.copy_p.get_repaymentSource(), GetData.repaymentSource_t)
        self.assertEqual(self.copy_p.get_signAddr(), GetData.signAddr_t)

    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
