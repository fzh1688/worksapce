from appium import webdriver

from page.basepage import BasePage
from page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity= "common.MainActivity"


    def start(self):

        #加if判断就是判断如果没有driver,就初始化driver,如果有driver,就直接启动activity
        if self._driver is None:
            caps={}
            caps["platformName"]="android"
            caps["deviceName"] = "emulator-5554"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            caps["noReset"] = True

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.start_activity(self._package,self._activity)
        self._driver.implicitly_wait(5)
        return self

    def main(self) -> Main:
        return Main(self._driver)









