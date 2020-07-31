import yaml
from appium.webdriver import webdriver
from selenium.webdriver.common.by import By


class BasePage:

    #初始化driver，只要继承了这个类的函数都可以用driver
    #init函数就是实例化对象，继承这个类的话，所有的函数都可以直接用该对象

    _driver : webdriver
    _black_list = [(By.ID,"iv_close")]
    #定义一个黑名单，如果黑名单里有东西，就进行点击  back_list里的值就是弹窗的关闭按钮的定位


    def __init__(self,driver: webdriver = None):
        self._driver = driver



    def find(self,locator,value):
        try:
            element = self._driver.find_element(locator,value)
            return element
        except:
            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    break
            return self.find(locator,value)

    # def click(self,locator,value):
    #     self.find(locator,value).click()


#测试步骤用yaml文件存储起来，用数据驱动方式
    def steps(self,path):
        with open(path) as f:
            steps=yaml.safe_load(f)
        element=None
        for step in steps:
            if "by" in step.keys():
                element=self.find(step["by"],step["locator"])
            if "action" in step.keys():
                action=step["action"]
                if action == "click":
                    element.click()
