from basepage import BasePage
from createproject_page import CreateNew
from lognuserinfo import LoanUserInfo
from projectstatus import ProjectSta
from uploadimg import UploadImg

class CopyPro(BasePage):
    url = ''

    @property
    def copy_btn(self):
        pass

    # 项目名称
    @property
    def project_name(self):
        return self.by_id("projectName")

    # 风险评级
    def custRating(self, custRating):
        return self.by_id('custRating' + custRating)

    # 保存信息
    @property
    def updateUserInfo(self):
        pass

    # 借款人信息标签
    @property
    def loanuserinfobtn(self):
        pass

    # 项目状态标签
    @property
    def projectstatusbtn(self):
        pass

    # 图片上传标签
    @property
    def uploadimgbtn(self):
        pass

    # 更改项目名称，加入风险评级（复制是不会复制风险评级，项目名称也太长）然后保存
    def save_proinfo(self, project_name='复制标的', custRating='D'):
        self.copy_btn.click()
        self.project_name.send_keys(project_name)
        self.custRating(custRating).click()
        self.updateUserInfo.click()

    # 切换到借款人信息标签
    def loanuserinfo(self):
        self.loanuserinfobtn.click()
        return LoanUserInfo(self.driver)

    # 切换到项目状态标签
    def projectstatus(self):
        self.projectstatusbtn.click()
        return ProjectSta(self.driver)

    # 切换到图片上传标签
    def uploadimgb(self):
        self.uploadimgbtn.click()
        return UploadImg