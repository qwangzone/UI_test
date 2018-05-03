#coding=utf-8
from basepage import BasePage


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
                   carRadiosid=1, carLoanRadios=1, scroll=0):
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
        self.scroll(scroll)
        self.savebtn.click()
