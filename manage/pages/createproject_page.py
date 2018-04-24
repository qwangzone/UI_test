from basepage import BasePage
from copyproject import CopyPro
import time
from datetime import datetime
class CreateNew(BasePage):
    url = "/loan/project/create"

    #项目名称
    @property
    def project_name(self):
        return self.by_id("projectName")

    #上线项目分类
    @property
    def project_category(self):
        return self.by_id("projectCategory")

    #项目类型
    @property
    def projectNewType(self):
        return self.by_id("projectNewType")

    #借款期限
    @property
    def financingMaturity(self):
        return self.by_id("financingMaturity")

    #标的类型
    @property
    def corporeType(self):
        return self.by_id("corporeType")

    #借款金额
    @property
    def amount(self):
        return self.by_id("amount")

    #最小认购金额元
    @property
    def minBidAmount(self):
        return self.by_id("minBidAmount")

    #还款方式
    @property
    def repaymentCalcType(self):
        return self.by_id("repaymentCalcType")

    #出借方年化利率
    @property
    def interestRatePercent(self):
        return self.by_id("interestRatePercent")

    #显示的年化利率
    @property
    def displayInterestRate(self):
        return self.by_id("displayInterestRate")

    #允许投标起始时间
    @property
    def start_time(self):
        pass

    #认购截止时间
    @property
    def end_time(self):
        pass

    #线上合同编号
    @property
    def contractFullID(self):
        pass

    #合同类型
    @property
    def contractType(self):
        pass

    #线下借款合同编号
    @property
    def loanContract(self):
        pass

    #风险评级
    def custRating(self, custRating):
        return self.by_id('custRating' + custRating)

    #借款人用户名
    @property
    def userName(self):
        pass

    #获取用户信息
    @property
    def btnLoadUser(self):
        pass

    #资金用途
    @property
    def purpose(self):
        pass

    #还款保障措施
    @property
    def houseGuaranteeInfo(self):
        pass

    #项目情况
    @property
    def projectDescription(self):
        pass

    #还款来源
    @property
    def repaymentSource(self):
        pass

    #底部保存按钮
    @property
    def saveLoanBtn(self):
        pass



    #填写创建标的字段
    def createnewproject(self, *,
                         project_name='test', project_category='信易融', projectNewType='直投',
                         financingMaturity=12, corporeType='普通标', amount=5000, minBidAmount=100,
                         repaymentCalcType='等额本息', interestRatePercent=10.5, displayInterestRate='',
                         start_time='', end_time='', contractFullID=222, contractType='信易融_薪金贷合同',
                         loanContract='w222', custRating='AAA', userName='v2998928', purpose='资金用途测试',
                         houseGuaranteeInfo='还款保障措施测试',projectDescription='项目情况测试',
                         repaymentSource='还款来源测试'):
        self.open()
        #先填写项目名称与借款期限
        self.project_name.send_keys(project_name)
        self.financingMaturity.send_keys(financingMaturity)
        time.sleep(2)
        self.project_category.send_keys(project_category)
        self.projectNewType.send_keys(projectNewType)
        self.corporeType.send_keys(corporeType)
        self.amount.send_keys(amount)
        self.minBidAmount.send_keys(minBidAmount)
        self.repaymentCalcType.send_keys(repaymentCalcType)
        self.interestRatePercent.send_keys(interestRatePercent)
        self.displayInterestRate.send_keys(displayInterestRate)
        self.start_time.send_keys(start_time)
        self.end_time.send_keys(end_time)
        self.contractFullID.send_keys(contractFullID)
        self.contractType.send_keys(contractType)
        self.loanContract.send_keys(loanContract)
        self.custRating(custRating).click()
        self.userName.send_keys(userName)
        #获取借款人信息
        self.btnLoadUser.click()
        self.purpose.send_keys(purpose)
        self.houseGuaranteeInfo.send_keys(houseGuaranteeInfo)
        self.projectDescription.send_keys(projectDescription)
        self.repaymentSource.send_keys(repaymentSource)
        self.saveLoanBtn.click()
        return CopyPro(self.diver)
        #self.repaymentSource.send_keys(kwargs['repaymentSource'])

    #获取创建成功标的后的url
    # def get_url(self):
    #     self.createnewproject()
    #     return self.driver.current_url()




