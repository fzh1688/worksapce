import pytest
import yaml

from pythoncode.calc import Calculator
calc = Calculator()
with open("../data/calcdata.yaml") as fr:
 data = yaml.safe_load(fr)
add_mydatas = list(data["add"].values())
add_myids = list(data["add"].keys())
sub_mydatas = list(data["sub"].values())
sub_myids = list(data["sub"].keys())
mul_mydatas = list(data["mul"].values())
mul_myids = list(data["mul"].keys())
div_mydatas = list(data["div"].values())
div_myids = list(data["div"].keys())

def setup_function():
    print("setup_function开始计算")

def teardown_function():
    print("teardown_function计算结束")

class TestCalc:


    #加法
    @pytest.mark.add
    @pytest.mark.parametrize(("a, b, result"), add_mydatas, ids=add_myids)
    def test_add(self,a,b,result):
        assert result == calc.add(a, b)

#减法
    @pytest.mark.sub
    @pytest.mark.parametrize(("a, b, result"), sub_mydatas, ids=sub_myids)
    def test_sub(self,a,b,result):
        assert result == calc.sub(a, b)

#乘法
    @pytest.mark.mul
    @pytest.mark.parametrize(("a, b, result"), mul_mydatas, ids=mul_myids)
    def test_mul(self,a,b,result):
        assert result == calc.mul(a, b)

#除法
    @pytest.mark.div
    @pytest.mark.parametrize(("a, b, result"), div_mydatas, ids=div_myids)
    def test_div(self,a,b,result):
        assert result == calc.div(a, b)




