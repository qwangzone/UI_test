# coding=utf-8
'''首页'''
from basepage import BasePage
from selenium import webdriver


class HomePage(BasePage):
    #关闭活动弹窗
    def layerclose(self):
        return self.by_css("div.layerbg>div.layerclose").click()
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

    #首页
    def index_link(self):
        return self.by_link("首页")

    #导航栏我要出借
    def lend_link(self):
        return self.by_link("我要出借")

    #导航栏信息披露
    def information_link(self):
        return self.by_link("信息披露")

    #导航栏风险教育
    def riskedc_link(self):
        return self.by_link("风险教育")

    #导航栏关于我们
    def aboutUs_link(self):
        return self.by_link("关于我们")

    #首页登录入口
    def login_link(self):
        return self.by_link("登录")

    #首页注册入口
    def register_link(self):
        return self.by_link("注册")

    #首页数据查看>
    def datashow(self):
        return self.by_link("查看>")

    #优选专区更多>
    def morepojects(self):
        return self.by_link("更多>")

    #优选专区更多
    def

    #邀请好友
    def invitefriends(self):
        return self.by_class_name("activespace")
        #return self.by_class_name("activespace mb3 b-r over-h")

    #转让专区
    def transfer(self):
        return self.by_class_name("area-item1")

    #活动专区
    def activities(self):
        return self.by_class_name("area-item2")

    #兑换专区
    def exchange(self):
        return self.by_class_name("area-item3")

    #新手专区
    def  Newbie(self):
        return self.by_class_name("area-item4")

    #页面下方关于我们
    def aboutUs_footer(self):
        return self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[1]")

    #页面下方新手指南
    def Newbie_footer(self):
        return self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[2]")

    #页面下方团队介绍
    def aboutteam_footer(self):
        return self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[3]")

    #页面下方帮助中心
    def helpcenter_footer(self):
        return self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[4]")

    #页面下方安全保障
    def  security_footer(self):
        return  self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[5]")

    #页面下方招贤纳士
    def  recruit_footer(self):
        return self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[6]")

    #页面下方风险提示
    def risktip_footer(self):
        return self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[7]")

    #页面下方联系我们
    def contactUs_footer(self):
        return self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[8]")

if __name__ == '__main__':

    dr = webdriver.Chrome()
    dr.maximize_window()
    dr.get('http://192.168.3.105/')
    hp = HomePage(dr)
    hp.layerclose()
    a = dr.find_element_by_class_name("area-item3")
    print(a)
    b = dr.find_element_by_xpath("//div[@class= 'foot-about float-l']/ul/li[4]").click()


