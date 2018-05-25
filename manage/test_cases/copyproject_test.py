#coding=utf-8
from selenium import webdriver
import unittest, os, sys

dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
import copyprojectpage, loginpage, createprojectpage
import configparser, os
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = dir + "/test_data/date.ini"
cf = configparser.ConfigParser()
cf.read(file_path, encoding="utf-8")
project_name_t = cf.get("manage_project_info", "project_name_t")
project_status = cf.get("manage_project_info", "project_status")
project_category_t = cf.get("manage_project_info", "project_category_t")
projectNewType_t = cf.get("manage_project_info", "projectNewType_t")
financingMaturity_t = cf.get("manage_project_info", "financingMaturity_t")
corporeType_t = cf.get("manage_project_info", "corporeType_t")
amount_t = cf.get("manage_project_info", "amount_t")
minBidAmount_t = cf.get("manage_project_info", "minBidAmount_t")
repaymentCalcType_t = cf.get("manage_project_info", "repaymentCalcType_t")
interestRatePercent_t = cf.get("manage_project_info", "interestRatePercent_t")
displayInterestRate_t = cf.get("manage_project_info", "displayInterestRate_t")
start_time_t = cf.get("manage_project_info", "start_time_t")
end_time_t = cf.get("manage_project_info", "end_time_t")
contractFullID_t = cf.get("manage_project_info", "contractFullID_t")
contractType_t = cf.get("manage_project_info", "contractType_t")
loanContract_t = cf.get("manage_project_info", "loanContract_t")
address = cf.get("manage_project_info", "address")
unicode = cf.get("manage_project_info", "unicode")
bondManId = cf.get("manage_project_info", "bondManId")
custRating_t = cf.get("manage_project_info", "custRating_t")
userName_t = cf.get("manage_project_info", "userName_t")
borrowerUserID = cf.get("manage_project_info", "borrowerUserID")
borrowerUserRealName = cf.get("manage_project_info", "borrowerUserRealName")
borrowerUserIDCard = cf.get("manage_project_info", "borrowerUserIDCard")
borrowerPayType = cf.get("manage_project_info", "borrowerPayType")
isRealBorrower = cf.get("manage_project_info", "isRealBorrower")
realBorrowerName = cf.get("manage_project_info", "realBorrowerName")
realBorrowerIdCard = cf.get("manage_project_info", "realBorrowerIdCard")
area = cf.get("manage_project_info", "area")
purpose_t = cf.get("manage_project_info", "purpose_t")
houseGuaranteeInfo_t = cf.get("manage_project_info", "houseGuaranteeInfo_t")
projectDescription_t = cf.get("manage_project_info", "projectDescription_t")
repaymentSource_t = cf.get("manage_project_info", "repaymentSource_t")
signAddr_t = cf.get("manage_project_info", "signAddr_t")

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
        self.assertEqual(self.copy_p.get_project_status(), project_status)
        self.assertEqual(self.copy_p.get_project_category(), project_category_t)
        self.assertEqual(self.copy_p.get_projectNewType(), projectNewType_t)
        self.assertEqual(self.copy_p.get_financingMaturity(), financingMaturity_t)
        self.assertEqual(self.copy_p.get_corporeType(), corporeType_t)
        self.assertEqual(self.copy_p.get_amount(), amount_t)
        self.assertEqual(self.copy_p.get_minBidAmount(), minBidAmount_t)
        self.assertEqual(self.copy_p.get_repaymentCalcType(), repaymentCalcType_t)
        self.assertEqual(self.copy_p.get_interestRatePercent(), interestRatePercent_t)
        self.assertEqual(self.copy_p.get_displayInterestRate(), displayInterestRate_t)
        self.assertEqual(self.copy_p.get_start_time(), start_time_t)
        self.assertEqual(self.copy_p.get_end_time(), end_time_t)
        self.assertEqual(self.copy_p.get_contractFullID(), contractFullID_t)
        self.assertEqual(self.copy_p.get_contractType(), contractType_t)
        self.assertEqual(self.copy_p.get_loanContract(), loanContract_t)
        self.assertEqual(self.copy_p.get_address(), address)
        self.assertEqual(self.copy_p.get_unicode(), unicode)
        self.assertEqual(self.copy_p.get_bondManId(), bondManId)
        self.assertEqual(self.copy_p.get_userName(), userName_t)
        self.assertEqual(self.copy_p.get_borrowerUserID(), borrowerUserID)
        self.assertEqual(self.copy_p.get_borrowerUserRealName(), borrowerUserRealName)
        self.assertEqual(self.copy_p.get_borrowerUserIDCard(), borrowerUserIDCard)
        self.assertEqual(self.copy_p.get_borrowerPayType(), borrowerPayType)
        self.assertEqual(self.copy_p.get_isrealborrower(), isRealBorrower)
        self.assertEqual(self.copy_p.get_realBorrowerName(), realBorrowerName)
        self.assertEqual(self.copy_p.get_realBorrowerIdCard(), realBorrowerIdCard)
        self.assertEqual(self.copy_p.get_area(), area)
        self.assertEqual(self.copy_p.get_purpose(), purpose_t)
        self.assertEqual(self.copy_p.get_houseGuaranteeInfo(), houseGuaranteeInfo_t)
        self.assertEqual(self.copy_p.get_projectDescription(), projectDescription_t)
        self.assertEqual(self.copy_p.get_repaymentSource(), repaymentSource_t)
        self.assertEqual(self.copy_p.get_signAddr(), signAddr_t)


    def tearDown(self):
        self.dr.quit()


if __name__ == '__main__':
    unittest.main()
