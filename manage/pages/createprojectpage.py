#coding=utf-8
from basepage import BasePage
from copyprojectpage import CopyPro
from loanuserinfopage import LoanUserInfo
from projectstatuspage import ProjectSta
from uploadimgpage import UploadImg
# import copyprojectpage
import time
from datetime import datetime, timedelta


class CreateNew(BasePage):
    url = "/loan/project/create"

    # 项目名称
    @property
    def project_name(self):
        return self.by_id("projectName")

    # 上线项目分类
    def project_category(self, text="信易融"):
        ele = self.by_id("projectCategory")
        self.select_by_text(ele, text)

    # 项目类型
    def projectNewType(self, text="直投"):
        ele = self.by_id("projectNewType")
        self.select_by_text(ele, text)

    # 借款期限
    @property
    def financingMaturity(self):
        return self.by_id("financingMaturity")

    # 标的类型
    def corporeType(self, text="普通标"):
        ele = self.by_id("corporeType")
        self.select_by_text(ele, text)

    # 借款金额
    @property
    def amount(self):
        return self.by_id("amount")

    # 最小认购金额元
    @property
    def minBidAmount(self):
        return self.by_id("minBidAmount")

    # 还款方式
    def repaymentCalcType(self, text="等额本息"):
        ele = self.by_id("repaymentCalcType")
        self.select_by_text(ele, text)

    # 出借方年化利率
    @property
    def interestRatePercent(self):
        return self.by_id("interestRatePercent")

    # 显示的年化利率
    @property
    def displayInterestRate(self):
        return self.by_id("displayInterestRate")

    # 允许投标起始时间
    def start_time(self, time_input=datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
        js = "document.getElementById('datetime-picker-4').value=\'%s\'" % time_input
        self.js_execute(js)

    # 认购截止时间
    def end_time(self, time_input=(datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")):
        js = "document.getElementById('datetime-picker-5').value=\'%s\'" % time_input
        self.js_execute(js)

    # 线上合同编号
    @property
    def contractFullID(self):
        return self.by_id("contractFullID")

    # 合同类型
    def contractType(self, text="信易融_薪金贷合同"):
        ele = self.by_id("contractType")
        self.select_by_text(ele, text)

    # 线下借款合同编号
    @property
    def loanContract(self):
        return self.by_id("loanContract")

    # 风险评级
    def custRating(self, custRating):
        return self.by_id('custRating' + custRating)

    # 借款人用户名
    @property
    def userName(self):
        return self.by_id("userName")

    # 获取用户信息
    @property
    def btnLoadUser(self):
        return self.by_id("btnLoadUser")

    # 资金用途
    @property
    def purpose(self):
        return self.by_id("purpose")

    # 还款保障措施
    @property
    def houseGuaranteeInfo(self):
        return self.by_id("houseGuaranteeInfo")

    # 项目情况
    @property
    def projectDescription(self):
        return self.by_id("projectDescription")

    # 还款来源
    @property
    def repaymentSource(self):
        return self.by_id("repaymentSource")

    # 签约地址
    @property
    def signAddr(self):
        return self.by_id("signAddr")

    # 底部保存按钮
    @property
    def saveLoanBtn(self):
        return self.by_id("saveLoanBtn")

    # 保存成功信息
    @property
    def success_alert(self):
        return self.by_class_name("alert-success")

    # 借款人信息标签
    @property
    def loanuserinfobtn(self):
        return self.by_link("借款人信息")

    # 项目状态标签
    @property
    def projectstatusbtn(self):
        return self.by_link("项目状态")

    # 图片上传标签
    @property
    def uploadimgbtn(self):
        return self.by_link("图片上传")

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
        return UploadImg(self.driver)

    # 获取保存成功信息
    def get_save_success_msg(self):
        return self.success_alert.text

    # 填写创建标的字段
    def createnewproject(self,
                         project_name='test', project_category='信易融', projectNewType='直投',
                         financingMaturity=12, corporeType='普通标', amount=5000, minBidAmount=100,
                         repaymentCalcType='等额本息', interestRatePercent="10.5", displayInterestRate='',
                         start_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                         end_time=(datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
                         contractFullID=222, contractType='信易融_薪金贷合同',
                         loanContract='w222', custRating='AAA',
                         userName='v2998928', purpose='资金用途测试',
                         houseGuaranteeInfo='还款保障措施测试', projectDescription='项目情况测试',
                         repaymentSource='还款来源测试', signAddr='签约地址测试'):
        # self.open()
        # 先填写项目名称与借款期限
        self.project_name.send_keys(project_name)
        self.financingMaturity.send_keys(financingMaturity)
        time.sleep(2)
        self.project_category(project_category)
        self.projectNewType(projectNewType)
        self.corporeType(corporeType)
        self.amount.clear()
        self.amount.send_keys(amount)
        self.minBidAmount.clear()
        self.minBidAmount.send_keys(minBidAmount)
        self.repaymentCalcType(repaymentCalcType)
        self.interestRatePercent.clear()
        self.interestRatePercent.send_keys(interestRatePercent)
        self.displayInterestRate.send_keys(displayInterestRate)
        self.start_time(start_time)
        self.end_time(end_time)
        self.contractFullID.send_keys(contractFullID)
        self.contractType(contractType)
        self.loanContract.send_keys(loanContract)
        self.custRating(custRating).click()
        self.userName.send_keys(userName)
        # 获取借款人信息
        self.btnLoadUser.click()
        self.purpose.clear()
        self.purpose.send_keys(purpose)
        self.houseGuaranteeInfo.clear()
        self.houseGuaranteeInfo.send_keys(houseGuaranteeInfo)
        self.projectDescription.clear()
        self.projectDescription.send_keys(projectDescription)
        self.repaymentSource.clear()
        self.repaymentSource.send_keys(repaymentSource)
        self.signAddr.send_keys(signAddr)
        self.saveLoanBtn.click()
        return CopyPro(self.driver)
        # self.repaymentSource.send_keys(kwargs['repaymentSource'])

        # 获取创建成功标的后的url
        # def get_url(self):
        #     self.createnewproject()
        #     return self.driver.current_url()
