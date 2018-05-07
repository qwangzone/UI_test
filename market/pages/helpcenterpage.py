'''帮助中心'''
from basepage import BasePage
from selenium import webdriver
class HelpCenterPage(BasePage):
    url = "/help/js"

    @property
    def content(self):
        return self.by_class_name("help-main")

    def get_content(self):
        return self.content.get_attribute("innerHTML")


if __name__ == '__main__':
    dr = webdriver.Chrome()
    dr.maximize_window()
    dr.get("http://192.168.3.10 5/help/js")
    a=dr.find_element_by_class_name("help-main").get_attribute("innerHTML")
    print(a)