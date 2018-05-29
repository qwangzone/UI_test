"""提现操作"""
from basepage import BasePage
import time

class DrawcashPage(BasePage):
    url = "/bindBankCard/withraw"

    #提现金额输入框
    def drawamount(self):
        return self.by_id("toCash")

    #提现按钮
    def draw_btn(self):
        return self.by_id("btn_send_code")

    #徽商电子账户交易密码
    def zhifu_btn(self):
        return self.by_id("encPin")

    #协议复选框
    def accept_btn(self):
        return self.by_id("mainAcceptIpt")

    #确认按钮
    def queren_btn(self):
        return self.by_id("sub")

    #提现金额
    def drawcash(self, drawamount='10'):
        self.drawamount().clear()
        self.drawamount().send_keys(drawamount)
        self.draw_btn().click()

    #徽商确认提现
    def huishang_queren(self, password='123456'):
        self.zhifu_btn().send_keys(password)
        self.accept_btn().click()
        self.queren_btn().click()

    #提现成功
    def drawsuccess_text(self):
        return self.by_id("succMsg").text

    #提交失败后服务器返回信息
    def drawfail_text(self):
        return self.by_xpath("//div[@class='credit-box txt-c']/ul/li[1]").text

    #可用余额
    def availableamount(self):
        return self.by_class_name("balance").text

    #提现金额输入不正确错误提示
    def drawinput_error(self):
        return self.by_id("toCasherror").text







