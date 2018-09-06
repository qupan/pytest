#coding=utf-8
import pytest

data=[(12,34),(-23,3)]

def add(x,y):
	z=x+y
	if z > 0:
		return True
	else:
		return False

@pytest.mark.parametrize('x,y',data)
def test_add(x,y):
	result=add(x,y)
	assert result == True,"失败原因，为负数"

if __name__=="__main__":
	pytest.main(['-s','test_004_parametrize.py','--html=../report/report.html'])
