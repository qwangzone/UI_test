from selenium import webdriver
import unittest, os, sys
import time
dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(dir + "/pages")
sys.path.append(dir + "/test_data")
from loginpage import LoginPage
from createprojectpage import CreateNew
from loanuserinfopage import LoanUserInfo
from get_data import GetData
from parameterized import parameterized


class LoanUserInfoTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.dr = webdriver.Chrome()
        self.dr.maximize_window()
        self.dr.implicitly_wait(10)
        # 后台需先登录
        self.login_p = LoginPage(self.dr)
        self.login_p.open()
        self.login_p.login()
        # 创建新标
        self.createpro_p = CreateNew(self.dr)
        self.createpro_p.open()
        self.createpro_p.createnewproject()
        self.loanuserinfo_p = self.createpro_p.loanuserinfo()
        self.loanuserinfo_p.submitform()
        self.LU = LoanUserInfo(self.dr)

    @parameterized.expand([('test_nativeProvince', 'get_nativeProvince', 'nativeProvince'),
                           ('test_companyEntryTime', 'get_companyEntryTime', 'companyEntryTime'),
                           ('test_currentAddress', 'get_currentAddress', 'currentAddress'),
                           ('test_ethnic', 'get_ethnic', 'ethnic'),
                           ('test_educationLevel', 'get_educationLevel', 'educationLevel'),
                           ('test_maritalStatus', 'get_maritalStatus', 'maritalStatus'),
                           ('test_yearOfService', 'get_yearOfService', 'yearOfService'),
                           ('test_get_quarters', 'get_quarters', 'quarters'),
                           ('test_natureOfCompany', 'get_natureOfCompany', 'natureOfCompany'),
                           ('test_get_industry', 'get_industry', 'industry'),
                           ('test_get_wage', 'get_wage', 'wage'),
                           ('test_get_province', 'get_province', 'province'),
                           ('test_get_city', 'get_city', 'city'),
                           ])
    def test_loanuserinfo(self, name, method, data):
        """借款人信息保存成功"""
        self.assertEqual(self.LU.get_all_loanuserinfo(method), GetData[data].value)

    # def test_companyEntryTime(self):
    #     self.assertEqual(self.LU.get_companyEntryTime(), GetData.companyEntryTime.value)
    #     self.assertEqual(self.LU.get_currentAddress(), GetData.currentAddress.value)
    #     self.assertEqual(self.LU.get_ethnic(), GetData.ethnic.value)
    #     self.assertEqual(self.LU.get_educationLevel(), GetData.educationLevel.value)
    #     self.assertEqual(self.LU.get_maritalStatus(), GetData.maritalStatus.value)
    #     self.assertEqual(self.LU.get_yearOfService(), GetData.yearOfService.value)
    #     self.assertEqual(self.LU.get_quarters(), GetData.quarters.value)
    #     self.assertEqual(self.LU.get_natureOfCompany(), GetData.natureOfCompany.value)
    #     self.assertEqual(self.LU.get_industry(), GetData.industry.value)
    #     self.assertEqual(self.LU.get_wage(), GetData.wage.value)
    #     self.assertEqual(self.LU.get_province(), GetData.province.value)
    #     self.assertEqual(self.LU.get_city(), GetData.city.value)

    @classmethod
    def tearDownClass(self):
        self.dr.quit()

if __name__ == '__main__':
    unittest.main()


