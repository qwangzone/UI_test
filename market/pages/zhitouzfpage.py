#coding=utf-8
from basepage import BasePage
import time

class InvestzfPage(BasePage):

    def zhifu_btn(self):
        return self.by_css(".dis-ib>button[name='btn_send_m_code']").click()

    def huishang(self, password):
        self.by_id("pass").send_keys(password)
        self.by_id("mainAcceptIpt").click()
        time.sleep(3)
        self.by_id("sub").click()


