'''主体披露'''
from basepage import BasePage


class MainPublishPage(BasePage):
    url = "/information/mainDisplay"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")


