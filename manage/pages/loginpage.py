#coding=utf-8
from basepage import BasePage
import time, functools


class LoginPage(BasePage):
    url = "/employee/login"

    @property
    def input_username(self):
        return self.by_id("UserName")

    @property
    def input_password(self):
        return self.by_id("UserPass")

    @property
    def input_yanzheng(self):
        return self.by_name("CaptchaInputText")

    @property
    def btn_click(self):
        return self.by_tag_name("button")

    @property
    def error_msg(self):
        return self.by_class_name("alert-error")

    @property
    def success_msg(self):
        return self.by_class_name("user-info")

    # 登录模块
    def login(self, username="caihongguang", password="789654", res="1111"):
        # self.open()
        self.input_username.send_keys(username)
        self.input_password.send_keys(password)
        time.sleep(5)
        self.input_yanzheng.send_keys(res)
        self.btn_click.click()

    def login_success(self):
        return functools.partial(self.login, username="caihongguang", password="789654", res="1111")

    # 获取页面报错信息
    def get_error_msg(self):
        return self.error_msg.text

    # 获取登录成功后的用户名
    def get_login_success_msg(self):
        return self.success_msg.text
