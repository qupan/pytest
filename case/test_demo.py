# -*- coding:utf-8 -*-
import pytest

'''命名规则，测试文件以test开头，测试类以Test开头，测试函数以test_开头'''

class TestDemo:

	@classmethod
	def setup_class(cls):
		print('所有用例之前执行')

	@classmethod
	def teardown_class(cls):
		print('dddd')

	def setup_method(self):
		print('每个用例之前执行')

	def teardown_method(self):
		print('每个用例之后执行')

	@pytest.mark.skip('ok')
	@pytest.mark.ok
	def test_001(self):
		assert 2==3
		print('eror')

	@pytest.mark.ok
	def test_002(self):
		assert 2==2
		print('eror')

	@pytest.mark.ok
	def test_003(self):
		assert 2==2
		print('eror')

if __name__=="__main__":
	pytest.main(['test_demo.py',#单个文件写入文件名字，否则就会运行case文件夹下所有用例
		'-q',#简化输出信息，保留核心信息
		'-v',#输出详细信息
		'-m','ok',#运行标记为ok的用例
		'-k','test_002',#选择固定名称的用例,可以使用and，or，not链接
		'--count=2',#全部用例运行两遍
		'--reruns=2',#失败的用例重新运行两遍j
		])
