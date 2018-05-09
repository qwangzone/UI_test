"""账户总览"""
from basepage import BasePage



class MyacountPage(BasePage):

    def login_success_text(self):
        return self.By_css("li.subNav>a").text

    # 风险承受能力
    def riskrate(self):
        return self.by_xpath("/html/body/div[6]/div[5]/div[1]/div[1]/div[2]/a").text


