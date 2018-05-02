from basepage import BasePage
# import os, sys
# dir = os.path.dirname(os.path.dirname(__file__))
# sys.path.append(dir)
# import create_data

class ProjetInfo(BasePage):
    url = "http://192.168.3.105/licai/"

    # 项目编号
    def project_number(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr/td[2]")

    # 项目类型
    def project_type(self):
        return self.by_xpath("//table[@class='details oddeven']/tbody/tr/td[4]")

    # 借款期限
    def project_deadline(self):
        pass


