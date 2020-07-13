import pytest
import yaml

'''
1、使用参数化数据驱动，完成加减乘除测试用例的自动生成
-2、修改测试用例为check_开头，修改测试用例的执行规则，执行所有check_开头和test_开头的测试用例
-3、控制测试用例顺序按照【加-减-乘-除】这个顺序执行,
-4、减法依赖加法， 除法依赖乘法
-5、注册一个命令行参数env,env默认值是test,表示测试环境，另外还有两个值 （dev,st）不同的环境读取不同的数据。
'''
from pythoncode.calc import Calculator

calc = Calculator()
with open("../data/calcdata.yaml") as f:
    datas = yaml.safe_load(f)

    adddatas = datas['add'].values()
    addids = datas['add'].keys()
    subdatas = datas['sub'].values()
    subids = datas['sub'].keys()
    multdatas = datas['mult'].values()
    multids = datas['mult'].keys()
    divdatas = datas['div'].values()
    divids = datas['div'].keys()

class TestCalc:

#加法
    @pytest.mark.add
    @pytest.mark.parametrize(("a, b, result"), adddatas, ids=addids)
    #@pytest.mark.flaky(reruns=5, reruns_delay=2)#设置失败重跑
    @pytest.mark.run(order=1)#设置用例执行的顺序
    @pytest.mark.dependency(name="add")
    def test_add(self,a,b,result):
        assert result == calc.add(a, b)

#动态生成测试用例
    def test_add1(self,param):
        print(f"param={param}")
        print("动态生成测试用例")

# 乘法
    @pytest.mark.mul
    @pytest.mark.parametrize(("a, b, result"), multdatas, ids=multids)
    @pytest.mark.run(order=3)
    @pytest.mark.dependency(name="mul")
    def test_mul(self,a,b,result):
        assert result == calc.mul(a, b)

#减法
    @pytest.mark.sub
    @pytest.mark.parametrize(("a, b, result"), divdatas, ids=divids)
    @pytest.mark.run(order=2)
    #@pytest.mark.dependency(depends=["add"])
    def test_sub(self,a,b,result):
        assert result == calc.sub(a, b)


#除法
    @pytest.mark.div
    @pytest.mark.parametrize('a,b,result',[(1,1,1)])
    @pytest.mark.run(order=4)
    @pytest.mark.dependency(depends=["mul"])
    def check_div(self,a,b,result):
         assert result == calc.div(a, b)


#获取url
    def test_getenv(self,cmdoption):
        env,datas=cmdoption
        ip=datas['env']['ip']
        port=datas['env']['port']
        url='http://'+str(ip)+":"+str(port)
        print(url)





