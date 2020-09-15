#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date      : 2020/7/13 22:29
# Author    : zzh
# @FileName : base.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from tool.logger import GetLogger
import time

log = GetLogger().get_logger()


class Base:
    def __init__(self, driver):
        log.info(f"正在初始化获取driver对象：{driver}")
        self.driver = driver

    def base_find_element(self, loc, timeout=10, poll_frequency=1):
        """
        找元素(加等待,显性等待) 缺省参数 在定义的函数的时候有默认参数
        :param loc: 定位路径
        :param timeout:延迟时间
        :param poll_frequency:轮询频率
        :return:元素
        """
        try:
            el = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
                lambda x: x.find_element(*loc))
            log.info(f"成功找到{loc}元素。")
            return el
        except Exception as e:
            log.error(f"没有找到{loc}元素！！！")
            self.base_get_image()
            raise e

    def base_find_elements(self, loc, timeout=10, poll_frequency=1):
        """
        找元素(加等待,显性等待) 缺省参数 在定义的函数的时候有默认参数
        :param loc: 定位路径
        :param timeout:延迟时间
        :param poll_frequency:轮询频率
        :return:元素
        """
        try:

            els = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency).until(
                lambda x: x.find_elements(*loc))
            log.info(f"成功找到这{loc}组元素。")
            return els
        except Exception as e:
            log.error(f"没有找到{loc}元素！！！")
            self.base_get_image()
            raise e

    def base_click(self, loc):
        """
        点击操作
        """
        try:
            self.base_find_element(loc).click()
            log.info(f"找到被点击的{loc}元素。")
        except Exception as e:
            log.error(f"点击{loc}元素没有被找到！！！")
            self.base_get_image()
            raise e

    def base_input(self, loc, value):
        """
        先清空后输入
        :param loc:
        :param info:
        :return:
        """
        log.info(f"正在输入：{loc}元素的值是:{value}。")
        self.base_find_element(loc).clear()
        self.base_find_element(loc).send_keys(value)

    def base_el_text(self, loc):
        """
        获取文本内容
        :param loc:
        :return:
        """
        try:

            log.info(f"正在获取{loc}元素的文本值为：{self.base_find_element(loc).text}")
            return self.base_find_element(loc).text
        except Exception as e:
            log.error(f"点击{loc}元素文本值没有找到！！！")
            self.base_get_image()
            raise e

    def base_get_image(self):
        """
        截图操作
        :return:
        """
        log.info("开始截图++++++")
        self.driver.get_screenshot_as_file('../image/{}.png'.format(time.strftime('%Y-%m-%d_%H_%M_%S')))

    def base_add_cookie(self, name, value):
        """
        添加cookie
        :param name:cookie名
        :param value:cookie值
        :return:
        """
        log.info("正在添加cookie++++++")
        self.driver.add_cookie({'name': name, 'value': value})

    def base_el_if_is_exist(self, loc):
        """
        如果可以找到元素，那么就返回True，找不到就返回False
        :param loc:
        :return:
        """
        try:
            self.base_find_element(loc)
            log.info(f"{loc}元素存在。")
            return True
        except:
            log.error(f"{loc}不存在！！！")
            self.base_get_image()
            return False

    def base_switch_window(self, title):
        """
        切换窗口
        """
        try:
            for handle in self.driver.window_handles:
                log.info('开始切换窗口')
                self.driver.switch_to.window(handle)
                if self.driver.title == title:
                    log.info('切换窗口成功')
                    break
        except Exception as e:
            log.error(f"{title}没找到！！！")
            self.base_get_image()
            raise e

    def base_switch_iframe(self, loc):
        """
        切换iframe
        """
        try:

            iframe = self.base_find_element(loc)
            self.driver.switch_to_frame(iframe)
            log.info("iframe窗口切换成功。")
        except Exception as e:
            log.error(f"{loc}定位错误，元素没找到！！！")
            self.base_get_image()
            raise e

    def base_default_content(self):
        """
        退出iframe
        """
        log.info("退出iframe")
        self.driver.switch_to.default_content()

    def base_click_index(self):
        loc = By.XPATH, '//*[@id="doc-topbar-collapse"]/ul/li[1]/a'
        self.base_click(loc)
        log.info('点击回到首页')

    @property
    def base_page_source(self):
        """
        加上@property这个就会把函数变成属性（函数不能传参）
        获取源码
        """
        log.info("获取源码")
        return self.driver.page_source

    def base_js(self, script):
        """
        执行js脚本
        """
        self.driver.execute_script(script)
        log.info(f"执行脚本：{script}")

    def base_max_window(self):
        self.driver.maximize_window()
        log.info("设置窗口最大行")

    def base_set_window(self, wide, high):
        '''
        Set browser window wide and high.

        Usage:
        driver.base_set_window(wide,high)
        '''
        self.driver.set_window_size(wide, high)
        log.info(" Set browser window %s wide and  %s high." % (wide, high))

    def base_get_attribute(self, loc, attribute):
        '''
        Gets the value of an element attribute.

        Usage:
        driver.base_get_attribute(By.CLASS_NAME, 'btn-go',"value")
        '''
        el = self.base_find_element(loc)
        log.info("Gets the value %s of an element attribute %s" % (attribute, loc))
        return el.get_attribute(attribute)

    def base_get_display(self, loc):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.base_get_display(By.CLASS_NAME, 'btn-go')
        '''
        el = self.base_find_element(loc)
        log.info("The %s element is exits or not" % loc)
        return el.is_displayed()

    def base_get_title(self):
        '''
        Get window title.

        Usage:
        driver.base_get_title()
        '''
        log.info("Get window title.")
        return self.driver.title

    def base_select(self, loc, value):
        '''
        Constructor. A check is made that the given element is, indeed, a SELECT tag. If it is not,
        then an UnexpectedTagNameException is thrown.

        :Args:
         - css - element SELECT element to wrap
         - value - The value to match against

        Usage:
            <select name="NR" id="nr">
                <option value="10" selected="">每页显示10条</option>
                <option value="20">每页显示20条</option>
                <option value="50">每页显示50条</option>
            </select>
            driver.base_select("#nr", '20')
            loc = By.CLASS_NAME, 'btn-go'
            driver.base_select(By.CLASS_NAME, 'btn-go', '20')
        '''
        # 先找到元素
        el = self.base_find_element(loc)
        # 实例化下拉框，获取select下拉框里面option的值
        Select(el).select_by_value(value)

    def base_forward(self):
        self.driver.forward()
        log.info("Click forward on current page.")

    def base_back(self):
        self.driver.back()
        log.info("Click back on current page.")

    def base_get_alert_text(self):
        '''
        Gets the text of the Alert.

        Usage:
        driver.base_get_alert_text()
        '''
        log.info("Gets the text of the Alert.")
        return self.driver.switch_to.alert.text

    def base_implicitly_wait(self, secs):
        '''
        Implicitly wait.All elements on the page.

        Usage:
        driver.base_implicitly_wait(10)
        '''
        self.driver.implicitly_wait(secs)
        log.info("wait for %d seconds." % secs)

    def base_accept_alert(self):
        '''
        Accept warning box.

        Usage:
        driver.base_accept_alert()
        '''
        self.driver.switch_to.alert.accept()
        log.info("Accept warning box.")

    def base_dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.base_dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()
        log.info("Dismisses the alert available.")


if __name__ == '__main__':
    from selenium import webdriver
    import time

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://121.42.15.146:9090/mtx/')
    base = Base(driver)
    # base.base_add_cookie('PHPSESSID', 'prdk5cbchgl6pavdofr9qs4b92')
    # driver.refresh(
    base.base_click(loc=(By.XPATH, '//div[@class="member-login"]/a[text()="登录"]'))
