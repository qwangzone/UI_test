#coding=utf-8
from basepage import BasePage
from copyprojectpage import CopyPro
from loanuserinfopage import LoanUserInfo
from projectstatuspage import ProjectSta
from uploadimgpage import UploadImg
# import copyprojectpage
import time

from datetime import datetime, timedelta
import configparser, os
dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = dir + "/test_data/date.ini"
cf = configparser.ConfigParser()
cf.read(file_path, encoding="utf-8")
project_name_t = cf.get("manage_project_info", "project_name_t")
project_category_t = cf.get("manage_project_info", "project_category_t")
projectNewType_t = cf.get("manage_project_info", "projectNewType_t")
financingMaturity_t = cf.get("manage_project_info", "financingMaturity_t")
corporeType_t = cf.get("manage_project_info", "corporeType_t")
amount_t = cf.get("manage_project_info", "amount_t")
minBidAmount_t = cf.get("manage_project_info", "minBidAmount_t")
repaymentCalcType_t = cf.get("manage_project_info", "repaymentCalcType_t")
interestRatePercent_t = cf.get("manage_project_info", "interestRatePercent_t")
displayInterestRate_t = cf.get("manage_project_info", "displayInterestRate_t")
start_time_t = cf.get("manage_project_info", "start_time_t")
end_time_t = cf.get("manage_project_info", "end_time_t")
contractFullID_t = cf.get("manage_project_info", "contractFullID_t")
contractType_t = cf.get("manage_project_info", "contractType_t")
loanContract_t = cf.get("manage_project_info", "loanContract_t")
custRating_t = cf.get("manage_project_info", "custRating_t")
userName_t = cf.get("manage_project_info", "userName_t")
purpose_t = cf.get("manage_project_info", "purpose_t")
houseGuaranteeInfo_t = cf.get("manage_project_info", "houseGuaranteeInfo_t")
projectDescription_t = cf.get("manage_project_info", "projectDescription_t")
repaymentSource_t = cf.get("manage_project_info", "repaymentSource_t")
signAddr_t = cf.get("manage_project_info", "signAddr_t")


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
    def start_time(self, time_input="2018-05-25 12:15:00""""datetime.now().strftime("%Y-%m-%d %H:%M:%S")"""):
        js = "document.getElementById('datetime-picker-4').value=\'%s\'" % time_input
        self.js_execute(js)

    # 认购截止时间
    def end_time(self, time_input="2020-05-25 12:15:00"""""(datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")"""):
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
                         project_name=project_name_t, project_category=project_category_t,
                         projectNewType=projectNewType_t,
                         financingMaturity=financingMaturity_t, corporeType=corporeType_t, amount=amount_t,
                         minBidAmount=minBidAmount_t,
                         repaymentCalcType=repaymentCalcType_t, interestRatePercent=interestRatePercent_t,
                         displayInterestRate=displayInterestRate_t,
                         start_time=start_time_t,
                         end_time=end_time_t,
                         contractFullID=contractFullID_t, contractType=contractType_t,
                         loanContract=loanContract_t, custRating=custRating_t,
                         userName=userName_t, purpose=purpose_t,
                         houseGuaranteeInfo=houseGuaranteeInfo_t, projectDescription=projectDescription_t,
                         repaymentSource=repaymentSource_t, signAddr=signAddr_t):
        # self.open()
        # 先填写项目名称与借款期限
        self.project_name.send_keys(project_name)
        self.financingMaturity.send_keys(financingMaturity)
       # time.sleep(2)
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

    def createprojectwrong(self,project_name='test', project_category='信易融',
                           projectNewType='直投',financingMaturity=12, corporeType='普通标'):
        # 先填写项目名称与借款期限
        self.project_name.send_keys(project_name)
        self.financingMaturity.send_keys(financingMaturity)

        self.project_category(project_category)
        self.projectNewType(projectNewType)
        self.corporeType(corporeType)
        self.amount.clear()
        self.minBidAmount.clear()
        self.interestRatePercent.clear()
        # 点击保存
        self.saveLoanBtn.click()

    # 获取alert文本并关闭alert
    def alert_text(self):
        text = self.switch_alert().text
        self.switch_alert().accept()
        return text

    # 获取报错的内容列表,0-9分别对应0-借款金额 必须填写，1-最小认购金额 必须填写，2-出借方年化利率 必须填写
    # 3-允许投标起始时间 必须填写，4-认购截止时间 必须填写，5-线上合同编号 必须填写，6-线下借款合同编号 必须填写，
    # 7-借款人用户ID 必须填写，8-资金用途 必须填写
    def get_error_text(self, index):
        return self.by_csses("span[class='field-validation-error']>span")[index].text

