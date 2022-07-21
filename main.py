#!/usr/bin/python
# -*- coding:utf-8 -*-
# author: vhow  python3
'''
注意！！！
本代码在chrome浏览器上自动测试
运行此代码需要selenium库和chromedriver
chromedriver版本为chrome的版本
本代码用的版本是 87.0.4280.88
通过下面的链接下载和你chrome版本相同的driver并放置于python.exe所在同级文件夹下
http://npm.taobao.org/mirrors/chromedriver/
代码跑起来后可最小化后台运行，或者开启静默模式不显示浏览器
'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import json


import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# 输入账号
student_id = input("手机号:")
# 输入密码
password = input("密码:")  
url = input("讨论区网址:")#注意！！！此处应打开学习通课程，返回旧版，复制网址到此处，每个人的都不一样！！！
#自定义讨论内容
tl1 = ("如何站点创建与制作商品简介页面")
tl2 = ("如何超链接应用与制作帮助信息页面")
tl3 = ("如何表格应用与制作购物车页面")
tl4 = ("如何表单应用与制作注册登录页面")
tl5 = ("如何网页布局与制作商品筛选页面")
tl6 = ("如何模板应用与制作商品推荐页面")
tl7 = ("如何网页特效与制作商品详情页面")
tl8 = ("如何网站整合与制作购物网站首页")
tl9 = ("如何搭建ASP.NET网站的运行与开发环境")
tl10 = ("如何使用控件高效创建网站页面")
tl11 = ("如何取用客户端和服务器的信息")
tl12 = ("如何控制网站页面的外观")
tl13 = ("如何快速实现网站的导航")
tl14 = ("如何新建商品目录")
tl15 = ("如何使用ADO.NET获取与处理数据")
tl16 = ("如何使用LINQ集成查询与更新数据")
tl17 = ("如何应用I0和流操纵文件和图片")
tl18 = ("如何整合与发布网站")
tl19 = ("三相异步电动机如何实现点动和自锁")
tl20 = ("举例说明PLC控制电机正反转在现实生活的应用")

# 打开chrome浏览器
driver = webdriver.Chrome()
# get请求网址
driver.get('http://i.chaoxing.com')
# 浏览器最大化 一定需要，否则会影响后面元素定位
driver.maximize_window()
# 设置浏览器大小
driver.set_window_size(1200, 700)
#以下是简单的
student_num = driver.find_element_by_xpath('//*[@id="phone"]')
student_num.send_keys(student_id)
student_pwd = driver.find_element_by_xpath('//*[@id="pwd"]')
student_pwd.send_keys(password)
driver.find_element_by_xpath('//*[@id="loginBtn"]').click()
#给1秒等待加载时间，以下不在详述
time.sleep(1)
#访问到讨论网址
driver.get(url)
time.sleep(1)

handles = driver.window_handles
driver.switch_to.window(handles[-1])

time.sleep(1)
#定位到讨论标题并输入自定义讨论内容1
driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl1)
time.sleep(0.5)
#点击确定，发送讨论内容
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()
#弹窗确定
driver.switch_to.alert.accept()
#以下同理
driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl2)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl3)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl4)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl5)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl6)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl7)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl8)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl9)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl10)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl11)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl12)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl13)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl14)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl15)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl16)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl17)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl18)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl19)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()

driver.find_element_by_xpath('//*[@id="c_title"]').send_keys(tl20)
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="addGroupTopicForm"]/div/div[1]/a[2]').click()

driver.switch_to.alert.accept()
time.sleep(5)

time.sleep(0.5)
# 关闭并释放资源
driver.quit()  # 关闭所有释放chromedriver资源


# 一些常用功能
# # 刷新
# driver.switch_to.alert.accept()
# # 返回
# driver.back()
# # 前进
# driver.forward()
# # 截图
# driver.get_screenshot_as_file('C:\\Users\\12559\\Desktop\\shot.jpg')
# # 获得当前url
# print(driver.current_url)
# # 获取页面源码
# print(driver.page_source)
# # 获取标题
# print(driver.title)
# driver.close() 关闭当前
