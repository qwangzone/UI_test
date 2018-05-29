"""注册页"""
from basepage import BasePage
from selenium import webdriver
import time
from registersuccesspage import RegisterSuccessPage

class RegisterPage(BasePage):

    url = "/user/register"

    #手机号码
    def mobile(self):
        return self.by_id("mobile")

    #登录密码
    def loginPass(self):
        return self.by_id("loginPass")

    #图形验证码
    def captchaCode(self):
        return self.by_id("captchaCode")

    #获取验证码按钮
    def btn_captchaCode(self):
        return self.by_tag_name("button")

    #输入短信验证码
    def sms_captchaCode(self):
        return self.by_id("mobileCode")

    #风险提示同意按钮
    def agreebtn(self):
        return self.by_class_name("agreebtn")

    #我有邀请码选填
    def inviteCode(self):
        return self.by_id("inviteCodeBox")

    #邀请码输入框
    def recommendCode(self):
        return self.by_id("recommendCode")

    #立即注册按钮
    def register_btn(self):
        return self.by_class_name("registerok")

    #注册
    def register(self, mobile='12345678915', password='123456', code='1', yanzheng='000000'):
        self.open()
        self.agreebtn().click()
        self.mobile().send_keys(mobile)
        self.loginPass().send_keys(password)
        self.captchaCode().send_keys(code)
        self.btn_captchaCode().click()
        time.sleep(3)
        self.sms_captchaCode().send_keys(yanzheng)
        self.register_btn().click()
        return RegisterSuccessPage(self.driver)

    def register_error(self, mobile='12345678910', password='123456', code='1'):
        self.open()
        self.agreebtn().click()
        self.mobile().send_keys(mobile)
        self.loginPass().send_keys(password)
        self.captchaCode().send_keys(code)
        self.btn_captchaCode().click()


    #手机号输入错误
    def mobile_error(self):
        return self.by_class_name("mobilem").text

    #登录密码设置格式错误
    def loginPass_error(self):
        return self.by_class_name("loginPassm").text

    #图形验证码输入错误
    def captchaCode_error(self):
        return self.by_class_name("captchaCodem").text

    #短信验证码输入错误
    def sms_error(self):
        return self.by_class_name("mobileCodem").text


if __name__ == '__main__':
    dr = webdriver.Chrome()
    dr.maximize_window()
    #dr.get('http://192.168.3.105/user/register')
    rp = RegisterPage(dr)
    rp.register()
    a = rp.mobile_error()
    print(a)
