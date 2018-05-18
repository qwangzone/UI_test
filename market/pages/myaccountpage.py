"""账户总览"""
from basepage import BasePage



class MyacountPage(BasePage):

    def login_success_text(self):
        return self.by_css("li.subNav>a").text

    # 风险承受能力
    def riskrate(self):
        return self.by_xpath("/html/body/div[6]/div[5]/div[1]/div[1]/div[2]/a").text

    #账户总资产
    def total_assets(self):
        return self.by_class_name("ft36").text

    #待收收入
    def due_income(self):
        return self.by_xpath("//table[@class='table']/tbody/tr[1]/td[2]").text

    #待收本金
    def due_prinple(self):
        return self.by_xpath("//table[@class='table']/tbody/tr[2]/td[2]").text

    #已赚收入
    def earned_income(self):
        return self.by_xpath("//table[@class='table']/tbody/tr[3]/td[2]").text

    #处理中金额
    def amount_in_process(self):
        return self.by_xpath("//table[@class='table']/tbody/tr[4]/td[2]").text

    #可用余额
    def avaliable_amount(self):
        return self.by_xpath("//div[@class='m-center randw pt1']/h1").text

    #登录成功用户名
    def login_user(self):
        return self.by_id("acountmobile").text


