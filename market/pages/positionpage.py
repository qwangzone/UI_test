'''联系我们'''
from basepage import BasePage
class PostionPage(BasePage):
    url = "/about/aboutus_ap"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")