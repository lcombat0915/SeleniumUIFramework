#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date      : 2020/7/13 22:28
# Author    : zzh
# @FileName : __init__.py.py
from selenium.webdriver.common.by import By
'''整个项目的配置项'''
# 项目的url
url = 'http://121.42.15.146:9090/mtx/'
'''以下是登录页面的配置信息'''
login_link = By.CSS_SELECTOR, '.menu-hd>a:nth-child(3)'
login_input_username = By.XPATH, '//label[text()="登录账号"]/following-sibling::input'
login_input_password = By.XPATH, '//label[text()="登录密码"]/following-sibling::input'
login_click_login_button = By.XPATH, '//button[text()="登录"]'

'''以下是删除购物车页面的配置信息'''
click_right_cart = By.XPATH, "(//*[text()='购物车'])[2]"
# click_delete_button = By.XPATH, '//*[@id="data-list-602"]/td[5]/a'
# click_confirm_delete = By.XPATH, "//*[text()='确定']"
click_delete_button = By.XPATH, '(//tbody/tr/td[5])[1]/a'
click_confirm_delete = By.XPATH, "//*[text()='确定']"
'''以下是加入购物车的配置信息'''
cart_search_input = By.ID, 'search-input'
cart_search_button = By.ID, 'ai-topsearch'
cart_into_detail = By.CSS_SELECTOR, 'ul.search-list>li:nth-child(1)'
cart_pink_spec = By.CSS_SELECTOR, 'li[data-value="粉色"]'
cart_size_spec = By.CSS_SELECTOR, 'li[data-value="M"]'
cart_add_cart = By.CSS_SELECTOR,"button[title='加入购物车']"
cart_detail_window_title = 'ZK爆款连衣裙'

''''以下是下订单的配置信息'''
order_window_title = '睡衣女长袖春秋季纯棉韩版女士大码薄款春夏季全棉家居服两件套装'
order_click_goods = By.XPATH, "(//div[@class='goods-list']/div[4]/a)[2]"
order_goods_color = By.XPATH, '//*[@data-value="白色"]'
order_goods_size = By.XPATH, '//*[@data-value="L"]'
ordre_click_buy_button = By.CSS_SELECTOR, '.buy-submit>button'
ordre_sec_pay = By.CSS_SELECTOR, '.payment>ul>li:nth-child(1)'
order_click_submit = By.CSS_SELECTOR,'.btn-go'
order_pay_success = By.CSS_SELECTOR, '.msg'