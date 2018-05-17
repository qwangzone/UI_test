'''首页tests'''
from basepage import BasePage
from selenium import webdriver


class HomePage(BasePage):

    url = "/"
    #关闭活动弹窗
    def layerclose(self):
        return self.by_css("div.layerbg>div.layerclose").click()

    # 页面顶部新浪微博
    def websina(self):
        js = 'document.getElementsByTagName("a")[0].target="";'
        #return self.by_class_name("wesina").click()
        self.js_execute(js)
        return self.by_class_name("wesina").click()

    # 页面顶部QQ群
    def weqq(self):
        return self.by_class_name("weqq").text

    # 页面顶部微信公众号
    def wechat(self):
        return self.by_class_name("wechat").text

    # 页面顶部客服电话
    def wetel(self):
        return self.by_class_name("wetel").text

    # 右上我要借款
    def borrow_right_head(self):
        return self.by_link("我要借款").click()

    # 帮助中心
    def helpcenter(self):
        return self.by_link("帮助中心").click()

    #首页
    def index_link(self):
        return self.by_link("首页").click()

    #导航栏我要出借
    def lend_link(self):
        return self.by_link("我要出借").click()

    #导航栏信息披露
    def information_link(self):
        return self.by_link("信息披露").click()

    #导航栏风险教育
    def riskedc_link(self):
        return self.by_link("风险教育").click()

    #导航栏关于我们
    def aboutUs_link(self):
        return self.by_link("关于我们").click()

    #首页登录入口
    def login_link(self):
        return self.by_link("登录").click()

    #首页注册入口
    def register_link(self):
        return self.by_link("注册").click()

    #首页累计交易额
    def accumulated_amount(self):
        amount1 = int(self.by_xpath("//div[@id='numscroll']/p/span[1]").text) * 10**8
        amount2 = int(self.by_xpath("//div[@id='numscroll']/p/span[2]").text) * 10**4
        amount3 = int(self.by_xpath("//div[@id='numscroll']/p/span[3]").text)
        return amount1 + amount2 + amount3

    #首页累计注册人数
    def accumulated_number(self):
        number1 = int(self.by_xpath("//p[@class='pl3']/span[1]").text) * 10**4
        number2 = int(self.by_xpath("//p[@class='pl3']/span[2]").text)
        return number1 + number2

    #首页数据查看>
    def datashow(self):
        return self.by_link("查看>").click()

    #优选专区更多>
    def morepojects(self):
        return self.by_link("更多>").click()

    #邀请好友
    def invitefriends(self):
        return self.by_class_name("activespace").click()
        #return self.by_class_name("activespace mb3 b-r over-h")

    #转让专区
    def transfer(self):
        return self.by_class_name("area-item1").click()

    #活动专区
    def activities(self):
        return self.by_class_name("area-item2").click()

    #兑换专区
    def exchange(self):
        return self.by_class_name("area-item3").click()

    #新手专区
    def  Newbie(self):
        return self.by_class_name("area-item4").click()

    #页面下方关于我们
    def aboutUs_footer(self):
        return self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[1]").click()

    #页面下方新手指南
    def Newbie_footer(self):
        return self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[2]").click()

    #页面下方团队介绍
    def aboutteam_footer(self):
        return self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[3]").click()

    #页面下方帮助中心
    def helpcenter_footer(self):
        return self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[4]").click()

    #页面下方安全保障
    def  security_footer(self):
        return  self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[5]").click()

    #页面下方招贤纳士
    def  recruit_footer(self):
        return self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[6]").click()

    #页面下方风险提示
    def risktip_footer(self):
        return self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[7]").click()

    #页面下方联系我们
    def contactUs_footer(self):
        return self.by_xpath("//div[@class= 'foot-about float-l']/ul/li[8]").click()
'''
if __name__ == '__main__':

    dr = webdriver.Chrome()
    dr.maximize_window()
    dr.get('http://192.168.3.105/')
    hp = HomePage(dr)
    hp.layerclose()
    a = dr.find_element_by_class_name("area-item3")
    print(a)
    b = str(dr.find_element_by_xpath("//div[@class= 'foot-about float-l']/ul/li[4]/a").get_attribute("href"))
    s = dr.current_url + b
    print(s)
    print(dr.current_url)
    a1 = hp.accumulated_amount()
    print(a1)
'''
