from time import sleep

from selenium.webdriver.common.by import By

from page.basepage import BasePage


class Main(BasePage):
    def goto_search(self):
        self.steps("../page/main.yaml")
        #self.find(By.ID,'tv_search').click()
    def goto_windows(self):
        #点击小笔的编辑按钮
        self.find(By.ID,"post_status").click()
        sleep(3)
        #点击搜索
        self.find(By.ID,"tv_search").click()
