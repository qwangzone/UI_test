#coding=utf-8
from basepage import BasePage
from loginpage import LoginPage
import time
from selenium import webdriver
from zhitouzfpage import InvestzfPage

class ZhitouXqPage(BasePage):
    url = "/licai/60232"

    #def listzhitou(self):
        #return self.by_xpath("//table[@class='licai-items-main']/tbody/tr[1]/td[7]")

    def amount_input(self):
        return self.by_id("amount")

    def submit_btn(self):
        return self.by_class_name("submitbtn")

    def queren(self):
        return self.by_id("okcp")

    def invest(self, money='100'):
        self.open()
        self.amount_input().send_keys(money)
        self.submit_btn().click()
        self.queren().click()
        time.sleep(3)
        return InvestzfPage()

    def input_error_text(self):
        return self.by_id("hint").text





