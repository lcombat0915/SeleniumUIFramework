#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date      : 2020/7/21 21:08
# Author    : zzh
# Python :v 3.7.3
from time import sleep
import page
from bases.base import Base


class PageOrder(Base):
    """mxt商城下订单"""

    def page_click_goods(self):
        """点击购买的商品"""
        self.base_click(page.order_click_goods)

    def page_move_scrollbar(self):
        """移动滚动条至最底部"""
        js = 'window.scrollTo(0,10000)'
        self.base_js(js)

    def page_goods_color_size(self):
        """选择商品颜色及尺寸"""
        sleep(1)
        self.base_click(page.order_goods_color)
        sleep(1)
        self.base_click(page.order_goods_size)

    def page_click_buy_button(self):
        """点击立即购买按钮"""
        self.base_click(page.ordre_click_buy_button)

    def page_sec_pay(self):
        """选择支付方式"""
        self.base_click(page.ordre_sec_pay)

    def page_click_submit_button(self):
        """点击提交订单按钮"""
        self.base_click(page.order_click_submit)

    def page_order(self):
        """
        组合业务：点击商品 > 提交订单
        """
        self.page_move_scrollbar()
        self.page_click_goods()
        self.base_switch_window(page.order_window_title)
        self.page_goods_color_size()
        self.page_click_buy_button()
        self.page_sec_pay()
        sleep(1)
        self.page_click_submit_button()


if __name__ == '__main__':
    from bases.driver import GetDriver
    from page.page_login import PageLogin

    driver = GetDriver().get_driver()
    PageLogin(driver).page_login_success()
    order = PageOrder(driver)
    order.page_order()
