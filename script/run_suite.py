#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date      : 2020/7/14 22:37
# Author    : zzh
# @FileName : run_suite.py
import unittest
from script.test_login import Login
from tool.HTMLTestRunner import HTMLTestRunner
import time
import os

# 执行单个文件中的测试用例
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(Login)
# 批量执行多个文件中测试用例
suite = unittest.defaultTestLoader.discover('script')
# 动态获取路径
file_dir = os.path.dirname(os.path.dirname(__file__))
file_path = file_dir + '/report/' + f'{time.strftime("%Y-%m-%d %H_%M_%S")}.html'
print('获取当前文件所在的目录:', os.path.dirname(__file__))
print('获取当前文件所在的上级路径的目录', file_dir)
print('拼接文件存放的绝对路径：', file_path)


with open(file_path, 'wb') as f:
    HTMLTestRunner(stream=f, title='码同学商城登录测试报告', description="登录测试用例执行结果").run(suite)

# 路径都是相对路径 ->入口文件(执行文件)
# suite = unittest.defaultTestLoader.loadTestsFromTestCase(Login)
# with open(f'../report/{time.strftime("%Y-%m-%d %H_%M_%S")}.html', 'wb') as f:
#     HTMLTestRunner(stream=f, title='码同学商城登录测试报告', description="登录测试用例执行结果").run(suite)
