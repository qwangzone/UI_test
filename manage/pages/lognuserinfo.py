from basepage import BasePage
class LoanUserInfo(BasePage):
    url = ''

    # 籍贯
    @property
    def nativeProvince(self):
        pass

    # 现公司入职时间
    @property
    def companyEntryTime(self):
        pass

    # 现居住地
    @property
    def currentAddress(self):
        pass

    # 民族
    @property
    def ethnic(self):
        pass

    # 学历
    @property
    def educationLevel(self):
        pass

    # 婚姻状况
    @property
    def maritalStatus(self):
        pass

    # 工作时间
    @property
    def yearOfService(self):
        pass

    # 工作岗位
    @property
    def quarters(self):
        pass

    # 公司性质
    @property
    def natureOfCompany(self):
        pass

    # 所属行业
    @property
    def industry(self):
        pass

    # 月收入
    @property
    def wage(self):
        pass

    # 工作城市
    @property
    def province(self):
        pass

    # 是否有房
    def houseRadios(self, houseRadiosid):
        pass

    # 是否有车
    def carRadios(self, carRadiosid):
        pass

    #填写借款人信息表单并提交
    def submitform(self, nativeProvince='山东青岛', companyEntryTime='2016-06-03', currentAddress='大理',
                   ethnic='土家族', educationLevel='本科', maritalStatus='未婚', yearOfService='20年以上',
                   quarters='股东', natureOfCompany='国有企业', industry='创造业', wage='30000元以上',
                   province='北京市北京市', houseRadiosid=1, carRadiosid=1):
        self.nativeProvince.send_keys(nativeProvince)
        self.companyEntryTime.send_keys(companyEntryTime)
        self.currentAddress.send_keys(currentAddress)
        self.ethnic.send_keys(ethnic)
        self.educationLevel.send_keys(educationLevel)
        self.maritalStatus.send_keys(maritalStatus)
        self.yearOfService.send_keys(yearOfService)
        self.quarters.send_keys(quarters)
        self.natureOfCompany.send_keys(natureOfCompany)
        self.industry.send_keys(industry)
        self.wage.send_keys(wage)
        self.province.send_keys(province)
        self.houseRadios(houseRadiosid).click()
        self.carRadios(carRadiosid).click()