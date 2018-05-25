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

    # 项目名称
    def get_project_name(self):
        return self.by_id("projectName").get_attribute("value")
    # 项目状态
    def get_project_status(self):
        return self.by_csses("div.control-group>div")[1].text

    # 上线项目分类
    def get_project_category(self):
        return self.by_css("#projectCategory>option:nth-child(2)").text.strip()

    # 项目类型
    def get_projectNewType(self):
        return self.by_css("#projectNewType>option:nth-child(1)").text.strip()

    # 借款期限
    def get_financingMaturity(self):
        return self.by_id("financingMaturity").get_attribute("value")

    # 标的类型
    def get_corporeType(self):
        return self.by_css("#corporeType>option:nth-child(1)").text.strip()

    # 借款金额
    def get_amount(self):
        return self.by_id("amount").get_attribute("value")

    # 最小认购金额
    def get_minBidAmount(self):
        return self.by_id("minBidAmount").get_attribute("value")

    # 还款方式
    def get_repaymentCalcType(self):
        return self.by_css("#repaymentCalcType>option:nth-child(3)").text.strip()

    # 出借方年化利率
    def get_interestRatePercent(self):
        return self.by_id("interestRatePercent").get_attribute("value")

    # 显示的年化利率
    def get_displayInterestRate(self):
        return self.by_id("displayInterestRate").get_attribute("value")

    # 允许投标时间
    def get_start_time(self):
        return self.by_id("datetime-picker-4").get_attribute("value")

    # 投标截至日期
    def get_end_time(self):
        return self.by_id("datetime-picker-5").get_attribute("value")

    # 线上合同编号
    def get_contractFullID(self):
        return self.by_id("contractFullID").get_attribute("value")

    # 合同类型
    def get_contractType(self):
        return self.by_css("#contractType>option:nth-child(1)").text.strip()

    # 线下合同编号
    def get_loanContract(self):
        return self.by_id("loanContract").get_attribute("value")

    # 丁方推荐人
    def get_address(self):
        return self.by_css("#address>option:nth-child(1)").text.strip()

    # 统一社会信用代码
    def get_unicode(self):
        return self.by_id("unicode").get_attribute("value")

    # 担保人
    def get_bondManId(self):
        return self.by_css("[name='bondManId']>option").text

    # 风险评级
    def get_custRatingAAA(self):
        return self.by_id("custRatingAAA").get_attribute("checked")

    # 借款人用户名
    def get_userName(self):
        return self.by_id("userName").get_attribute("value")

    # 借款人用户id
    def get_borrowerUserID(self):
        return self.by_id("borrowerUserID").get_attribute("value")

    # 借款人真实姓名
    def get_borrowerUserRealName(self):
        return self.by_id("borrowerUserRealName").get_attribute("value")

    # 借款人身份证
    def get_borrowerUserIDCard(self):
        return self.by_id("borrowerUserIDCard").get_attribute("value")

    # 借款人缴费方式
    def get_borrowerPayType(self):
        return self.by_css("#borrowerPayType>option").text.strip()

    # 借款人是否实际借款人
    def get_isrealborrower(self):
        return self.by_css("#isrealborrower>option").text

    # 实际借款人姓名
    def get_realBorrowerName(self):
        return self.by_id("realBorrowerName").get_attribute("value")

    # 实际借款人身份证id
    def get_realBorrowerIdCard(self):
        return self.by_id("realBorrowerIdCard").get_attribute("value")

    # 项目区域位置
    def get_area(self):
        return self.by_id("area").get_attribute("value")

    # 资金用途
    def get_purpose(self):
        return self.by_id("purpose").get_attribute("value")

    # 还款保障措施
    def get_houseGuaranteeInfo(self):
        return self.by_id("houseGuaranteeInfo").text

    # 项目情况
    def get_projectDescription(self):
        return self.by_id("projectDescription").text

    # 还款来源
    def get_repaymentSource(self):
        return self.by_id("repaymentSource").text

    # 签约地址
    def get_signAddr(self):
        return self.by_id("signAddr").get_attribute("value")



