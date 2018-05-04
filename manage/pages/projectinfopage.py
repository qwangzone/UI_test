#coding=utf-8
from basepage import BasePage
# import os, sys
# dir = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(dir)
# import create_data

class ProjetInfo(BasePage):
    url = "http://192.168.3.105/licai/"

    # 项目编号
    def project_number(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr[1]/td[2]")
        #return self.ele_wait_present(self, '')
    # 项目类型
    def project_type(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr[1]/td[4]")

    # 借款期限
    def project_deadline(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr[2]/td[2]")

    #借款金额
    def project_amount(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr[2]/td[4]")

    #借款用途
    def project_use(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr[3]/td[2]")

    #签约地点
    def project_Addr(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr[3]/td[4]")

    #募集开始时间
    def project_sartt(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr[4]/td[2]")

    #起息日
    def value_date(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr[6]/td[2]")

    #最小出借金额
    def bid_amount(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr[6]/td[4]")

    #还款方式
    def repayment_type(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr[7]/td[2]")

    #还款来源
    def repayment_origin(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr[8]/td[2]")

    #还款保障措施
    def repayment_assurance(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr[9]/td[2]")

    #项目风险评估
    def risk_rating(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr[10]/td[2]")

    #学历
    def education_background(self):
        return self.by_xpath("//table[@class='details']/tbody/tr[3]/td[4]")

    #婚姻状况
    def marriage_status(self):
        return self.by_xpath("//table[@class='details']/tbody/tr[4]/td[4]")

    #从事行业
    def industry_info(self):
        return self.by_xpath("//table[@class='details']/tbody/tr[6]/td[2]")

    #企业性质
    def enterprise_property(self):
        return self.by_xpath("//table[@class='details']/tbody/tr[6]/td[4]")

    #岗位职务
    def position_info(self):
        return self.by_xpath("//table[@class='details']/tbody/tr[7]/td[2]")

    #月收入
    def income_monthly(self):
        return self.by_xpath("//table[@class='details']/tbody/tr[7]/td[4]")

    #是否有房
    def house_Radios(self):
        return self.by_xpath("//table[@class='details']/tbody/tr[8]/td[2]")

    #是否有房贷
    def house_loan(self):
        return self.by_xpath("//table[@class='details']/tbody/tr[8]/td[4]")

    #是否有车
    def car_Radios(self):
        return self.by_xpath("//table[@class='details']/tbody/tr[9]/td[2]")

    #是否有车贷
    def car_loan(self):
        return self.by_xpath("//table[@class='details']/tbody/tr[9]/td[4]")

    #所在城市
    def living_city(self):
        return self.by_xpath("//table[@class='details']/tbody/tr[10]/td[2]")