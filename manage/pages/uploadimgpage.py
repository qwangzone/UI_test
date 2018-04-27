# coding=utf-8
from basepage import BasePage
from selenium.webdriver.common.keys import Keys
import time

class UploadImg(BasePage):
    url = ''

    # 身份证正面上传
    @property
    def CardFrond(self):
        return self.by_id("uploadLocallyCardFrond")

    # 身份证反面上传
    @property
    def CardBack(self):
        return self.by_id("uploadLocallyCardBack")

    # 借款人头像上传
    @property
    def LocallyHead(self):
        return self.by_id("uploadLocallyHead")

    # 上传图片
    @property
    def sendimg(self):
        return self.by_id("uploadImageLocalInputCardFrond")

    # 弹框上保存按钮
    @property
    def submit_save_btn(self):
        return self.by_id("saveFileBtnCardFrond")

    # 关闭弹窗
    def close_alert(self):
        return self.by_xpath("/html/body/div[7]/div/div[2]/button")

    def uploadimage(self, imgpath="D:\测试用图\\1.png"):
        self.CardFrond.click()
        self.sendimg.send_keys(imgpath)
        time.sleep(1)
        self.submit_save_btn.click()
        self.switch_alert.accept()
