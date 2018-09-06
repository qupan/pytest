#coding=utf-8
import pytest,sys

@pytest.mark.skipif(sys.platform != 'win32',reason ='test')
class TestDemo:

	def setup(self):
		print('每个用例开始前执行')

	def teardown(self):
		print('每个用例结束后执行')

	def setup_class(self):
		print('所有用例之前执行')

	def teardown_class(self):
		print('所有用例之后执行')

	#@pytest.mark.skip(reason='no')
	def test_one(self):
		x='this'
		assert 'h' in x
	#@pytest.mark.skipif(2<3,reason='no')
	def test_two(self):
		x='hello'
		assert hasattr(x,'check')

if __name__=="__main__":
	pytest.main(['-s','test_001.py'])
