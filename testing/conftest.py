import pytest

#scope=seession   整个项目只调用一次
#scope=module  每一个模块就是每个.py文件都执行一次
#登录方法添加了autouse=True  其他测试用例不用调用登录方法，也会去执行登录方法
import yaml

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

#命令行去添加一个参数
def pytest_addoption(parser):
    mygroup=parser.getgroup("hogwarts")
    mygroup.addoption("--env",
                      default='test',
                      dest='env',
                      help='set your run env'

    )
@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env",default='test')
    if myenv =='test':
        datapath = '../data/test/env.yaml'

    if myenv =='dev':
        datapath = '../data/dev/env.yaml'

    with open(datapath) as f:
        datas=yaml.safe_load(f)

    return myenv,datas

#通过方法动态的生成测试用例
def pytest_generate_tests(metafunc: "Metafunc") -> None:
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param",
                             metafunc.module.adddatas,
                             ids=metafunc.module.addids,
                             scope='function')



