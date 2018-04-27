from basepage import BasePage


class ProjectSta(BasePage):
    url = ''

    # 标的状态按钮
    def changestatusbtn(self):
        return self.by_xpath("//div[@id='contact-info']/div/form[1]/input[3]")

    # 中止按钮
    def discontinuebtn(self):
        return self.by_xpath("//div[@id='contact-info']/div/form[2]/input[3]")

    # 改变项目状态
    def changeprosta(self):
        self.changestatusbtn().click()

    # 中止项目
    def stoppro(self):
        self.discontinuebtn().click()