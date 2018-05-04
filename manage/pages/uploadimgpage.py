# coding=utf-8
from basepage import BasePage
from selenium.webdriver.common.keys import Keys
import time, os, sys


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

    # 上传身份证正面图片
    @property
    def sendimgFrond(self):
        return self.by_id("uploadImageLocalInputCardFrond")

    # 上传身份证反面图片
    @property
    def sendimgBack(self):
        return self.by_id("uploadImageLocalInputCardBack")

    # 上传身份证头像图片
    @property
    def sendimgHead(self):
        return self.by_id("uploadImageLocalInputHead")

    # 弹框上保存正面按钮
    @property
    def submit_save_Frond_btn(self):
        return self.by_id("saveFileBtnCardFrond")

    # 弹框上保存反面按钮
    @property
    def submit_save_Back_btn(self):
        return self.by_id("saveFileBtnCardBack")

    # 弹框上保存头像按钮
    @property
    def submit_save_Head_btn(self):
        return self.by_id("saveFileBtnHead")

    # 关闭弹窗
    def close_alert(self):
        return self.by_xpath("/html/body/div[7]/div/div[2]/button")

    def uploadimage(self, imgfronk=r"E:\github\UI_test\manage\\testdate_img\1.png",
                    imgback=r"E:\github\UI_test\manage\\testdate_img\2.png",
                    imghead=r"E:\github\UI_test\manage\\testdate_img\3.png"):
        # 上传身份证正面
        self.CardFrond.click()
        self.ele_wait_present(("id", "uploadImageLocalInputCardFrond")).send_keys(imgfronk)
        # self.sendimgFrond.send_keys(imgfronk)
        time.sleep(1)
        #self.ele_wait_visible(("id", "saveFileBtnCardFrond")).click()
        self.ele_wait_clickable(("id", "saveFileBtnCardFrond")).click()
        #self.submit_save_Frond_btn.click()
        time.sleep(1)
        #self.ele_wait_visible(("xpath", "/html/body/div[7]/div/div[2]/button")).click()
        self.ele_wait_clickable(("xpath", "/html/body/div[7]/div/div[2]/button")).click()
        # self.close_alert().click()
        # time.sleep(1)

        # 上传身份证反面
        self.CardBack.click()
        self.ele_wait_present(("id", "uploadImageLocalInputCardBack")).send_keys(imgback)
        # self.sendimgBack.send_keys(imgback)
        time.sleep(1)
        #self.ele_wait_visible(("id", "saveFileBtnCardBack")).click()
        self.ele_wait_clickable(("id", "saveFileBtnCardBack")).click()
        # self.submit_save_Back_btn.click()
        time.sleep(1)
        #self.ele_wait_visible(("xpath", "/html/body/div[7]/div/div[2]/button")).click()
        self.ele_wait_clickable(("xpath", "/html/body/div[7]/div/div[2]/button")).click()

        # self.close_alert().click()
        # time.sleep(1)

        # 上传身份证头像
        self.LocallyHead.click()
        self.ele_wait_present(("id", "uploadImageLocalInputHead")).send_keys(imghead)
        # self.sendimgHead.send_keys(imghead)
        time.sleep(1)
        #self.ele_wait_visible(("id", "saveFileBtnHead")).click()
        self.ele_wait_clickable(("id", "saveFileBtnHead")).click()
        # self.submit_save_Head_btn.click()
        time.sleep(1)
        #self.ele_wait_visible(("xpath", "/html/body/div[7]/div/div[2]/button")).click()
        self.ele_wait_clickable(("xpath", "/html/body/div[7]/div/div[2]/button")).click()

        # self.close_alert().click()
        # time.sleep(1)
        # btn_dic = {self.CardFrond: [self.sendimgFrond, self.submit_save_Frond_btn],
        #            self.CardBack: [self.sendimgBack, self.submit_save_Back_btn],
        #            self.LocallyHead: [self.sendimgHead, self.submit_save_Head_btn]}
        # for i, v in btn_dic.items():
        #     i().click()
        #     v[0].send_keys(imgpath)
        #     time.sleep(1)
        #     v[1].click()
        #     time.sleep(1)
        #     self.close_alert().click()
        #     time.sleep(5)
