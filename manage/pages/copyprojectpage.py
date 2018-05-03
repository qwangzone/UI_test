#coding=utf-8
from basepage import BasePage
from loanuserinfopage import LoanUserInfo
from projectstatuspage import ProjectSta
from uploadimgpage import UploadImg
#from createprojectpage import CreateNew
#import createprojectpage

class CopyPro(BasePage):
    url = ''
    @property
    def copy_btn(self):
        return self.by_link("复制项目")

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
        return self.by_id("updateUserInfo")

    # # 借款人信息标签
    # @property
    # def loanuserinfobtn(self):
    #     return self.by_link("借款人信息")
    #
    # # 项目状态标签
    # @property
    # def projectstatusbtn(self):
    #     return self.by_link("项目状态")
    #
    # # 图片上传标签
    # @property
    # def uploadimgbtn(self):
    #     return self.by_link("图片上传")

    # 保存成功信息
    @property
    def success_alert(self):
        return self.by_class_name("alert-success")

    # 获取保存成功信息
    def get_save_success_msg(self):
        return self.success_alert.text

    # 更改项目名称，加入风险评级（复制是不会复制风险评级，项目名称也太长）然后保存
    def save_proinfo(self, project_name='复制标的', custRating='D', scroll=0):
        self.copy_btn.click()
        self.project_name.clear()
        self.project_name.send_keys(project_name)
        self.custRating(custRating).click()
        self.scroll(scroll)
        self.updateUserInfo.click()

    # # 切换到借款人信息标签
    # def loanuserinfo(self):
    #     self.loanuserinfobtn.click()
    #     return LoanUserInfo(self.driver)
    #
    # # 切换到项目状态标签
    # def projectstatus(self):
    #     self.projectstatusbtn.click()
    #     return ProjectSta(self.driver)
    #
    # # 切换到图片上传标签
    # def uploadimgb(self):
    #     self.uploadimgbtn.click()
    #     return UploadImg(self.driver)
