from basepage import BasePage

class RegisterSuccessPage(BasePage):

    def register_success(self):
        return self.by_class_name("register-user")
        #return self.by_xpath("//div[@class='register-box2 bg-fff mt2 mb2']/ul/li[1]")