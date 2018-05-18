#coding=utf-8
'''登录页'''
from basepage import BasePage
from homepage import HomePage
from myaccountpage import MyacountPage
import time
from selenium import webdriver

class LoginPage(BasePage):
    url = "/user/login"

    def input_userName(self):
        return self.by_id("mobile")

    def input_loginPass(self):
        return self.by_id("loginPass")

    def input_yanzheng(self):
        return self.by_id("captchaCode")

    def login_btn(self):
        return self.by_class_name("registerok")

    def register_link(self):
        return self.by_link("立即注册")

    def homepage_link(self):
        return self.by_link("返回首页")

    def mobilem_error(self):
        return self.by_class_name("mobilem")

    def loginPassm_error(self):
        return self.by_class_name("loginPassm")

    def captchaCodem_error(self):
        return self.by_class_name("captchaCodem")

    #登录操作
    def login(self, username, password, yanzhengma):
        self.open()
        self.input_userName().send_keys(username)
        self.input_loginPass().send_keys(password)
        self.input_yanzheng().send_keys(yanzhengma)
        #time.sleep(5)
        self.login_btn().click()
        time.sleep(3)
        return MyacountPage(self.driver)

    #获取用户名输入框错误提示
    def mobilem_error_text(self):
        return self.mobilem_error().text

    #获取登录密码输入框错误提示
    def loginPassm_error_text(self):
        return self.loginPassm_error().text

    #获取验证码输入框错误提示
    def captchaCodem_error_text(self):
        return self.captchaCodem_error().text

'''
    #跳转至注册页
    def register(self):
        self.open()
        dr = webdriver.Chrome()
        login_window = dr.current_window_handle
        self.register_link().click()
        time.sleep(5)
        all_handles = dr.window_handles
        for handle in all_handles:
            if handle != login_window:
                dr.switch_to_window(handle)
                self.by_class_name("agreebtn").click()

if __name__ == '__main__':
    dr = webdriver.Chrome()
    dr.maximize_window()
    login = LoginPage(dr)
    login.login()
    time.sleep(5)
    a = login.captchaCodem_error_text()
    print(a)
'''