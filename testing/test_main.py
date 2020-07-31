import pytest
import yaml
from selenium.webdriver.common.by import By

from page.app import App


class TestMain:

    #@pytest.mark.parametrize("value1,value2",yaml.safe_load(open("./test_main.yaml")))
    def test_main(self,value1,value2):
        # print(value1)
        # print(value2)
        app=App()
        app.start().main().goto_search()
    def test_windows(self):
        app = App()
        app.start().main().goto_windows()








