#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date      : 2020/7/14 22:27
# Author    : zzh
# @FileName : test_login.py

import unittest

from bases.driver import GetDriver
from page.page_login import PageLogin
from bases.opendriver import OpenDriver
import ddt

from tool.readExceldata_list import ReadExcelDataList
from tool.readExcelData_dict import ReadExcelDataDict

"""
week6-1作业 一作业需求：读取列表套列表的数据结构，然后对test_login进行参数化操作
"""
# data = [{'username': 'z01', 'password': 'nihao'},
#         {'username': 'tom', 'password': ' '},
#         {'username': '!@~!@~', 'password': '56161'},
#         ]

# 逆向用例
# test_data = ReadExcelDataList().get_excel_data() # 列表嵌套列表
test_data = ReadExcelDataDict().get_excel_data(['username', 'password'])  # 列表嵌套字典


@ddt.ddt
class Login(unittest.TestCase):
    """
    业务逻辑层
    类属性->全局变量，类方法和实例方法都可以调用
    """
    driver = None
    login = None

    @classmethod
    def setUpClass(cls) -> None:
        """
        前置函数->打开浏览器
        创建浏览器对象，打开登录页面
        """
        # 调用opendriver模块实现
        # cls.driver = OpenDriver().get_driver('ch')
        # cls.driver.maximize_window()
        # cls.driver.get(page.url)
        # cls.login = PageLogin(cls.driver)

        # 调用driver封装模块实现
        cls.driver = GetDriver().get_driver()
        cls.login = PageLogin(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        """
        后置函数->关闭浏览器
        :return:
        """
        # cls.driver.quit()
        GetDriver().close_driver()

    @ddt.data(*test_data)
    def test_login(self, data):
        # 调用登录业务, 读取data进行测试

        # 参数化1：列表嵌套列表
        # self.login.page_login(data[0], data[1])

        # 参数化2：列表嵌套字典
        self.login.page_login(data['username'], data['password'])

        # 断言，登录成功返回Ture，否则返回False
        result = self.login.page_el_if_is_exist()
        self.assertTrue(result)
