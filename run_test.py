# -*- coding:utf-8 -*-
import pytest,time

'''运行所有用例，并生成html，tap，xml报告'''

if __name__=="__main__":
	name=time.strftime('%Y_%m_%d-%H-%M-%S')
	pytest.main(['-q',#简化输出信息，保留核心内容
		'-s',#运行所有的用例
		'--html=report/HTML/%s report.html'%name,#生成HTML格式报告
		'--self-contained-html',#将HTML报告和css文件合并成一个
		'--tap-outdir=report/TAP',#使用tap指出存放目录
		'--tap-combined',#将所有tap合并存放
		'--junitxml=report/XML/%s report.xml'%name,#生成xml文件
		'--count=2', #全部用例运行两遍
		'--reruns=2',#失败的用例重新运行两遍
	    '--setup-show',#回溯fixture的运行过程	
		])
