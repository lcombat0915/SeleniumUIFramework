#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date      : 2020/7/19 21:47
# Author    : zzh
# Python :v 3.7.3
from time import sleep

import page
from bases.base import Base


class PageCart(Base):
    """mtx商城购物车"""

    def page_click_right_cart(self):
        """点击右上角的购物车链接"""
        self.base_click(page.click_right_cart)

    def page_click_delete_button(self):
        """点击删除按钮"""
        self.base_click(page.click_delete_button)

    def page_click_confirm_button(self):
        """点击确定按钮"""
        self.base_click(page.click_confirm_delete)

    def page_if_delete_button_exist(self):
        """删除按钮是否存在"""
        self.base_el_if_is_exist(page.click_delete_button)

    def page_input_good_name(self, goods):
        """输入框输入商品名字"""
        self.base_input(page.cart_search_input, goods)

    def page_click_search_button(self):
        """点击搜索按钮"""
        self.base_click(page.cart_search_button)

    def page_click_goods(self):
        """点击商品"""
        # self.base_find_element(page.cart_into_detail)
        self.base_click(page.cart_into_detail)
        self.base_switch_window(page.cart_detail_window_title)

    def page_click_goods_spec(self):
        """点击商品规格"""
        self.base_click(page.cart_pink_spec)
        sleep(2)
        self.base_click(page.cart_size_spec)
        self.base_click(page.cart_add_cart)

    def page_delete(self):
        """组合业务，删除功能"""
        self.page_click_right_cart()
        self.page_click_delete_button()
        self.page_click_confirm_button()

    def page_add(self, goos):
        """添加购物车"""
        self.page_input_good_name(goos)
        self.page_click_search_button()
        self.page_click_goods()
        self.page_click_goods_spec()
