#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date      : 2020/7/21 22:45
# Author    : zzh
# Python :v 3.7.3
import unittest
from time import sleep
import page
from bases.driver import GetDriver
from page.page_login import PageLogin
from page.page_order import PageOrder


class TestOrder(unittest.TestCase):
    """
    week6-3作业 一作业需求：order提交订单的测试用例编写
    """
    driver = None
    order = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = GetDriver().get_driver()
        PageLogin(cls.driver).page_login_success()
        cls.order = PageOrder(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        GetDriver().close_driver()

    def test_place_order(self):
        """下订单功能测试"""
        self.order.page_order()
        sleep(2)
        # 断言查找支付成功元素
        self.assertTrue(self.order.base_el_if_is_exist(page.order_pay_success))


if __name__ == '__main__':
    unittest.main()
