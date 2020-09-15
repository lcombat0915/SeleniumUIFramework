#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date      : 2020/7/19 21:46
# Author    : zzh
# Python :v 3.7.3
import unittest
import time
from bases.driver import GetDriver
from page.page_cart import PageCart
from page.page_login import PageLogin


class TestCart(unittest.TestCase):
    """测试购物车"""
    # driver = None
    # cart = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        # 调用登录成功方法
        PageLogin(cls.driver).page_login_success()
        time.sleep(2)
        # 实例化购物车页面
        cls.cart = PageCart(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().close_driver()

    # 每一个函数执行完之后都会执行一次
    def tearDown(self) -> None:
        # 点击首页
        self.cart.base_click_index()

    def test_add_cart(self):
        # try...except..捕获异常 目的：为了截图,截图之后把错误信息抛出去
        self.cart.page_add('雪纺连衣裙')
        time.sleep(2)
        self.assertIn('加入成功', self.cart.base_page_source)

    def test_cart_delete(self):
        """测试删除购物车的商品"""
        self.cart.page_delete()
        time.sleep(1)
        self.assertFalse(self.cart.page_if_delete_button_exist())
