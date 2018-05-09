'''高管团队'''
from basepage import BasePage
class CompanyTeamPage(BasePage):
    url = "/about/aboutus_team"

    @property
    def content(self):
        return self.by_class_name("xf_mainRight")

    def get_content(self):
        return self.content.get_attribute("innerHTML")
