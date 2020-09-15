#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date      : 2020/7/14 21:30
# Author    : zzh
# @FileName : driver.py
import page
from bases.opendriver import OpenDriver
import sys
import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)
# print(os.pardir)
# sys.path.append(os.pardir)

class GetDriver:
    """
    driver封装
    """
    driver = None

    @classmethod
    def get_driver(cls):
        """
        获取driver
        :param browser:
        :return:
        """
        if cls.driver is None:
            cls.driver = OpenDriver().get_driver()
            cls.driver.maximize_window()
            cls.driver.get(page.url)
            return cls.driver

    @classmethod
    def close_driver(cls):
        """
        为了程序的健壮性，需要先判断不为空的时候再执行
        :return:
        """
        if cls.driver:
            cls.driver.quit()
            # print('========', cls.driver)
            # 必须置空
            cls.driver = None


if __name__ == '__main__':
    gd = GetDriver()
    driver = gd.get_driver()
    gd.close_driver()
