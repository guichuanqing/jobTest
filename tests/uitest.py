# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/15 10:17
# @File : uitest.py
# Description : 文件说明
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="D:\\ProgramData\\Anaconda3\\Scripts\\chromedriver.exe")
# 初始化 WebDriver
driver = webdriver.Chrome(service=service)  # 如果使用 Chrome 浏览器

# 打开百度
driver.get("https://www.baidu.com")

# 查找搜索框并输入关键词
search_box = driver.find_element(By.ID, "kw")
search_box.send_keys("Selenium")

# 提交搜索
search_box.send_keys(Keys.RETURN)

# 等待几秒钟，以便观察结果
time.sleep(5)

# 关闭浏览器
driver.quit()

