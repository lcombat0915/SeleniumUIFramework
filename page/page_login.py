#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date      : 2020/7/14 21:58
# Author    : zzh
# @FileName : page_login.py

import time
from bases.base import Base
import page

'''
不变的东西(重复的)需要封装
变得东西当做参数，你想传什么就传什么
'''


class PageLogin(Base):
    """mtx商城登录页面"""

    def page_click_login_link(self):
        """
        点击登录链接前缀page 页面层 见名知意  loc元素定位
        :return:
        """
        self.base_click(page.login_link)

    def page_input_username(self, username):
        """
        输入用户名
        :param username:
        :return:
        """
        self.base_input(page.login_input_username, username)

    def page_input_password(self, password):
        """
        输入密码
        :param password:
        :return:
        """
        self.base_input(page.login_input_password, password)

    def page_click_login_button(self):
        """
        点击登录  修改超时时间和频率
        :return:
        """
        self.base_click(page.login_click_login_button)

    def page_el_if_is_exist(self):
        """
        判断元素是否存在
        :return:
        """
        time.sleep(3)
        return self.base_el_if_is_exist(page.login_link)

    def page_login(self, username, password):
        """
        组合业务逻辑->跟你做功能测试一样的一个组合的动作，动作顺序一样
        :param username:
        :param password:
        :return:
        """
        self.page_click_login_link()
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_button()

    def page_login_success(self):
        """
        组合业务逻辑->跟你做功能测试一样的一个组合的动作，动作顺序一样
        :param username:
        :param password:
        :return:
        """
        self.page_click_login_link()
        self.page_input_username('zzh01')
        self.page_input_password('a123456')
        self.page_click_login_button()


if __name__ == '__main__':
    from selenium import webdriver

    dr = webdriver.Chrome()
    dr.maximize_window()
    dr.get(page.url)
    login = PageLogin(dr)
    login.page_login('zzh01', 'a123456')
    assert login.page_el_if_is_exist() == False
