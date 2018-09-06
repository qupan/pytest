#coding=utf-8
import pytest,time
'''
运行所有用例
'''
if __name__=="__main__":
	report_name=time.strftime('%Y_%m_%d-%H-%M-%S')
	pytest.main(['-s','--html=report/html/%s report.html'%report_name,
		'--resultlog=report/log/%s report.log'%report_name,
		'--junitxml=report/xml/%s report.xml'%report_name])
