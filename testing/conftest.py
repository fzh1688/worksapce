import pytest

#scope=seession   整个项目只调用一次
#scope=module  每一个模块就是每个.py文件都执行一次
#登录方法添加了autouse=True  其他测试用例不用调用登录方法，也会去执行登录方法
from pythoncode.calc import Calculator


@pytest.fixture()
def fix_calc():
    cal = Calculator()
    print("【开始计算】")
    yield cal
    print("【计算结束】")

@pytest.fixture()
def login():
    print("登陆")
    # yield 激活fixture的teardown方法
    # print(request.param[0])
    yield ['username', 'password']
    print("teardown")
