"""充值金额页面"""
from basepage import BasePage
from sumapaypage import SumapayPage
import time

class RechargePage(BasePage):
    url = "/recharge"

    #输入充值金额
    def recharge_amount(self):
        return self.by_id("amount")

    #选择网银支付银行
    def icbc_btn(self):
        return self.by_id("icbc")

    #选择确认按钮
    def queren_btn(self):
        #js = 'document.getElementById("confirm").target="";'
        #self.js_execute(js)
        return self.by_id("confirm")

    #充值
    def recharge(self, money='10'):
        self.recharge_amount().send_keys(money)
        self.icbc_btn().click()
        self.queren_btn().click()
        return SumapayPage(self.driver)

