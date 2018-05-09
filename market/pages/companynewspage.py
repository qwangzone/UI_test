'''公司动态'''
from basepage import BasePage
class CompanyNewsPage(BasePage):
    url = "/notice/dynamic"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")
