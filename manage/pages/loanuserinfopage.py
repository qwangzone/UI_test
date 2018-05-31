"""借款人信息"""
from basepage import BasePage
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
file_path = dir + "/test_data/"
sys.path.append(file_path)
from get_data import GetData


class LoanUserInfo(BasePage):
    url = ''

    # 籍贯
    @property
    def nativeProvince(self):
        return self.by_id("nativeProvince")

    # 现公司入职时间
    @property
    def companyEntryTime(self):
        return self.by_id("companyEntryTime")

    # 现居住地
    @property
    def currentAddress(self):
        return self.by_id("currentAddress")

    # 民族
    def ethnic(self, text="汉族"):
        ele = self.by_name("ethnic")
        self.select_by_text(ele, text)

    # 学历
    def educationLevel(self, text="本科"):
        ele = self.by_name("educationLevel")
        self.select_by_text(ele, text)

    # 婚姻状况
    def maritalStatus(self, text="未婚"):
        ele = self.by_name("maritalStatus")
        self.select_by_text(ele, text)

    # 工作时间
    def yearOfService(self, text="20年以上"):
        ele = self.by_name("yearOfService")
        self.select_by_text(ele, text)

    # 工作岗位
    def quarters(self, text="普通员工"):
        ele = self.by_name("quarters")
        self.select_by_text(ele, text)

    # 公司性质
    def natureOfCompany(self, text="国有企业"):
        ele = self.by_name("natureOfCompany")
        self.select_by_text(ele, text)

    # 所属行业
    def industry(self, text="采矿业"):
        ele = self.by_name("industry")
        self.select_by_text(ele, text)

    # 月收入
    def wage(self, text="5000元以下"):
        ele = self.by_name("wage")
        self.select_by_text(ele, text)

    # 工作城市（省份）
    def province(self, text="北京市"):
        ele = self.by_name("province")
        self.select_by_text(ele, text)

    # 工作城市
    def city(self, text="北京市"):
        ele = self.by_name("city")
        self.select_by_text(ele, text)

    # 是否有房
    def houseRadios(self, houseRadiosid=1):
        return self.by_id("houseRadios" + str(houseRadiosid))

    # 有无房贷
    def houseLoanRadios(self, houseLoanRadios=1):
        return self.by_id("houseLoanRadios" + str(houseLoanRadios))

    # 是否有车
    def carRadios(self, carRadiosid=1):
        return self.by_id("carRadios" + str(carRadiosid))

    # 有无车贷
    def carLoanRadios(self, carLoanRadios=1):
        return self.by_id("carLoanRadios" + str(carLoanRadios))

    # 保存按钮
    @property
    def savebtn(self):
        return self.by_id("updateLoanUserInfo")

    # 填写借款人信息表单并提交
    def submitform(self, nativeProvince='山东青岛', companyEntryTime='2016-06-03', currentAddress='大理',
                   ethnic='土家族', educationLevel='本科', maritalStatus='未婚', yearOfService='20年以上',
                   quarters='股东', natureOfCompany='国有企业', industry='创造业', wage='30000元以上',
                   province='北京市', city="北京市", houseRadiosid=1, houseLoanRadios=1,
                   carRadiosid=1, carLoanRadios=1):
        self.nativeProvince.clear()
        self.nativeProvince.send_keys(nativeProvince)
        self.companyEntryTime.clear()
        self.companyEntryTime.send_keys(companyEntryTime)
        self.currentAddress.clear()
        self.currentAddress.send_keys(currentAddress)
        self.ethnic(ethnic)
        self.educationLevel(educationLevel)
        self.maritalStatus(maritalStatus)
        self.yearOfService(yearOfService)
        self.quarters(quarters)
        self.natureOfCompany(natureOfCompany)
        self.industry(industry)
        self.wage(wage)
        self.province(province)
        self.city(city)
        self.houseRadios(houseRadiosid).click()
        self.houseLoanRadios(houseLoanRadios).click()
        self.carRadios(carRadiosid).click()
        self.carLoanRadios(carLoanRadios).click()
        self.scroll(0)
        self.savebtn.click()

    # 获取姓名
    def get_userrealBorrowerName(self):
        return self.by_id("userrealBorrowerName").get_attribute("value")

    # 获取籍贯
    def get_nativeProvince(self):
        return self.by_id("nativeProvince").get_attribute("value")

    # 入职时间
    def get_companyEntryTime(self):
        return self.by_id("companyEntryTime").get_attribute("value")

    # 现居住地
    def get_currentAddress(self):
        return self.by_id("currentAddress").get_attribute("value")

    # 民族
    def get_ethnic(self):
        return self.by_name("ethnic").find_element_by_css_selector("[value='Tujia']").text

    # 学历
    def get_educationLevel(self):
        return self.by_name("educationLevel").find_element_by_css_selector("[value='UNDERGRADUATE']").text

    # 婚姻情况
    def get_maritalStatus(self):
        return self.by_name("maritalStatus").find_element_by_css_selector("[value='SINGLE']").text

    # 工作时间
    def get_yearOfService(self):
        return self.by_name("yearOfService").find_element_by_css_selector("[value='YEAR_ABOVE_20']").text

    # 工作岗位
    def get_quarters(self):
        return self.by_name("quarters").find_element_by_css_selector("[value='SHAREHOLDER']").text

    # 公司性质
    def get_natureOfCompany(self):
        return self.by_name("natureOfCompany").find_element_by_css_selector("[value='NatureOfCompany1']").text

    # 所属行业
    def get_industry(self):
        return self.by_name("industry").find_element_by_css_selector("[value='industry3']").text

    # 月收入
    def get_wage(self):
        return self.by_name("wage").find_element_by_css_selector("[value='WageTypeMore30000']").text

    # 工作城市（省）
    def get_province(self):
        return self.by_name("province").find_element_by_css_selector("[value='1']").text

    # 工作城市（市）
    def get_city(self):
        return self.by_name("city").find_element_by_css_selector("[value='2']").text

    # 是否有房
    def get_houseRadios1(self):
        return self.by_id("houseRadios1").get_attribute("value")

    # 有无房贷
    def get_houseLoanRadios1(self):
        return self.by_id("houseLoanRadios1").get_attribute("value")

    # 是否有车
    def get_carRadios1(self):
        return self.by_id("carRadios1").get_attribute("value")

    # 有无车贷
    def get_carLoanRadios1(self):
        return self.by_id("carLoanRadios1").get_attribute("value")

    def get_all_loanuserinfo(self, index):
        get_nativeProvince = self.get_nativeProvince()
        get_companyEntryTime = self.get_companyEntryTime()
        get_currentAddress = self.get_currentAddress()
        get_ethnic = self.get_ethnic()
        get_educationLevel = self.get_educationLevel()
        get_maritalStatus = self.get_maritalStatus()
        get_yearOfService = self.get_yearOfService()
        get_quarters = self.get_quarters()
        get_natureOfCompany = self.get_natureOfCompany()
        get_industry = self.get_industry()
        get_wage = self.get_wage()
        get_province = self.get_province()
        get_city = self.get_city()
        info_ls = {}
        info_ls['get_nativeProvince'] = get_nativeProvince
        info_ls['get_companyEntryTime'] = get_companyEntryTime
        info_ls['get_currentAddress'] = get_currentAddress
        info_ls['get_ethnic'] = get_ethnic
        info_ls['get_educationLevel'] = get_educationLevel
        info_ls['get_maritalStatus'] = get_maritalStatus
        info_ls['get_yearOfService'] = get_yearOfService
        info_ls['get_quarters'] = get_quarters
        info_ls['get_natureOfCompany'] = get_natureOfCompany
        info_ls['get_industry'] = get_industry
        info_ls['get_wage'] = get_wage
        info_ls['get_province'] = get_province
        info_ls['get_city'] = get_city
        return info_ls[index]





