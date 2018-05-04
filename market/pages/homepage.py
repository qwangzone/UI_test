# coding=utf-8
'''首页'''
from basepage import BasePage


class HomePage(BasePage):
    # 页面顶部新浪微博
    def websina(self):
        return self.by_class_name("wesina")

    # 页面顶部QQ群
    def weqq(self):
        return self.by_class_name("weqq")

    # 页面顶部微信公众号
    def wechat(self):
        return self.by_class_name("wechat")

    # 页面顶部客服电话
    def wetel(self):
        return self.by_class_name("wetel")

    # 右上我要借款
    def borrow_right_head(self):
        return self.by_link("我要借款")

    # 帮助中心
    def helpcenter(self):
        return self.by_link("帮助中心")

