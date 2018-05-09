'''网贷知识'''
from basepage import BasePage
class NetLoanKnowPage(BasePage):
    url = "/risktip/wdzs"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")