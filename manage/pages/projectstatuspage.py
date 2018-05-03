#coding=utf-8
from basepage import BasePage


class ProjectSta(BasePage):
    url = ''

    # 标的状态按钮
    def changestatusbtn(self):
        return self.by_xpath("//div[@id='contact-info']/div/form[1]/input[3]")

    # 中止按钮
    def discontinuebtn(self):
        return self.by_xpath("//div[@id='contact-info']/div/form[2]/input[3]")

    # 改变项目状态 已安排
    def changeprosta_yianpai(self):
        self.changestatusbtn().click()
        # self.changestatusbtn().click()
        # self.ele_wait(self.changestatusbtn()).click()

    # 改变项目状态 开放投标
    def changeprosta_kaifang(self):
        self.changestatusbtn().click()
    # 中止项目
    def stoppro(self):
        self.discontinuebtn().click()