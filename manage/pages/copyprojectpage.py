#coding=utf-8
from basepage import BasePage
import os, sys
dir = os.path.dirname(os.path.dirname(__file__))
file_path = dir + "/test_data/"
sys.path.append(file_path)
from get_data import GetData

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
    def save_proinfo(self, project_name=GetData.project_name_t.value, custRating=GetData.custRating_t.value, scroll=0):
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

    def get_all_info(self, index):
        project_name = self.get_project_name()
        project_status = self.get_project_status()
        project_category = self.get_project_category()
        projectNewType = self.get_projectNewType()
        financingMaturity = self.get_financingMaturity()
        corporeType = self.get_corporeType()
        amount = self.get_amount()
        minBidAmount = self.get_minBidAmount()
        repaymentCalcType = self.get_repaymentCalcType()
        interestRatePercent = self.get_interestRatePercent()
        displayInterestRate = self.get_displayInterestRate()
        start_time = self.get_start_time()
        end_time = self.get_end_time()
        contractFullID = self.get_contractFullID()
        contractType = self.get_contractType()
        loanContract = self.get_loanContract()
        address = self.get_address()
        unicode = self.get_unicode()
        bondManId = self.get_bondManId()
        custRatingAAA = self.get_custRatingAAA()
        userName = self.get_userName()
        borrowerUserID = self.get_borrowerUserID()
        borrowerUserRealName = self.get_borrowerUserRealName()
        borrowerUserIDCard = self.get_borrowerUserIDCard()
        borrowerPayType = self.get_borrowerPayType()
        isrealborrower = self.get_isrealborrower()
        realBorrowerName = self.get_realBorrowerName()
        realBorrowerIdCard = self.get_realBorrowerIdCard()
        area = self.get_area()
        purpose = self.get_purpose()
        houseGuaranteeInfo = self.get_houseGuaranteeInfo()
        projectDescription = self.get_projectDescription()
        repaymentSource = self.get_repaymentSource()
        signAddr = self.get_signAddr()
        info_ls = {}
        info_ls['project_name'] = project_name
        info_ls['project_status'] = project_status
        info_ls['project_category'] = project_category
        info_ls['projectNewType'] = projectNewType
        info_ls['financingMaturity'] = financingMaturity
        info_ls['corporeType'] = corporeType
        info_ls['amount'] = amount
        info_ls['minBidAmount'] = minBidAmount
        info_ls['repaymentCalcType'] = repaymentCalcType
        info_ls['interestRatePercent'] = interestRatePercent
        info_ls['displayInterestRate'] = displayInterestRate
        info_ls['start_time'] = start_time
        info_ls['end_time'] = end_time
        info_ls['contractFullID'] = contractFullID
        info_ls['contractType'] = contractType
        info_ls['loanContract'] = loanContract
        info_ls['address'] = address
        info_ls['unicode'] = unicode
        info_ls['bondManId'] = bondManId
        info_ls['custRatingAAA'] = custRatingAAA
        info_ls['userName'] = userName
        info_ls['borrowerUserID'] = borrowerUserID
        info_ls['borrowerUserRealName'] = borrowerUserRealName
        info_ls['borrowerUserIDCard'] = borrowerUserIDCard
        info_ls['borrowerPayType'] = borrowerPayType
        info_ls['isrealborrower'] = isrealborrower
        info_ls['realBorrowerName'] = realBorrowerName
        info_ls['realBorrowerIdCard'] = realBorrowerIdCard
        info_ls['area'] = area
        info_ls['purpose'] = purpose
        info_ls['houseGuaranteeInfo'] = houseGuaranteeInfo
        info_ls['projectDescription'] = projectDescription
        info_ls['repaymentSource'] = repaymentSource
        info_ls['signAddr'] = signAddr
        return info_ls[index]





class get_method():
    def test(self):
        return "0"

    def test1(self):
        return "1"

    def test2(self):
        return '2'

    def wq(self, index):
        a = self.test()
        b = self.test1()
        c = self.test2()
        w = {'a':a, 'b':b, 'c':c}
        return w[index]

    def __iter__(self):
        return self

    def __next__(self):
        self.a = self.test()
        self.b = self.test1()
        self.c = self.test2()
        return self.a




