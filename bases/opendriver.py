#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date      : 2020/7/14 21:18
# Author    : zzh
# @FileName : opendriver.py
'''
封装一个具体的浏览器，然后获取哪一个浏览器的driver
'''
from selenium import webdriver


class OpenDriver:
    def get_driver(self, browser='ch'):
        """
        浏览器drive人的封装过程
        :param browser:
        :return:浏览器
        """
        if browser == 'firfox' or browser == 'ff':
            return webdriver.Firefox()
        elif browser == 'chrome' or browser == 'ch':
            return webdriver.Chrome()
        elif browser == 'internet explorer' or browser == 'ie':
            return webdriver.Ie()
        else:
            raise NameError(f'Not found {browser} browser,you must input "firefox","ff","chrome","ie"')


if __name__ == '__main__':
    od = OpenDriver()
    driver = od.get_driver('ch')
