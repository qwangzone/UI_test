from basepage import BasePage
import time

class SumapayPage(BasePage):
    url= ''

    # 银行卡号
    def cardnumber(self):
        #return self.by_xpath("//form[@id='payform']/table/tbody/tr[6]/td[2]")
        return self.by_id("CARD_NO")

    # 卡密码
    def password(self):
        return self.by_id("PASSWORD")

    # 支付按钮
    def pay_btn(self):
        return self.by_xpath("//form[@id='payform']/table/tbody/tr[8]/td[1]/input[1]")

    #支付后点击返回才回调
    def return_btn(self):
        return self.by_xpath("//form[@id='retrunform']/table/tbody/tr[6]/td/input[1]")

    #输入测试卡信息进行充值
    def sumapay(self, cardnumber='4417120412174596', password='289017'):
        self.cardnumber().send_keys(cardnumber)
        self.password().send_keys(password)
        self.pay_btn().click()
        time.sleep(2)
        self.return_btn().click()
