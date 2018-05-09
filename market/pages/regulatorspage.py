'''监管部门'''
from basepage import BasePage


class RegulatorsPage(BasePage):
    url = "/information/superDep"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")
