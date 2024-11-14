# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/14 10:56
# @File : ui_job.py
# Description : 文件说明
"""
import logging
from typing import Dict, Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import keys
from jobtest.jobs.base_job import BaseJob

logger = logging.getLogger(__name__)

class UiJob(BaseJob):
    """UI 测试任务，继承自 BaseJob，执行 UI 测试逻辑。"""
    def __init__(self, name: str, config: Dict = None, input_data: Any = None):
        super().__init__(name, config, input_data)
        self.level = "ui" # 定义该 Job 属于 UI 测试层级

    def execute(self):
        """执行 UI 测试，模拟用户在浏览器中的交互行为。"""
        logger.info(f"Running UI test for Job: {self.name}")
        # 初始化 Selenium WebDriver
        driver = webdriver.Chrome(executable_path= self.config.get("driver_path", "/path/to/chromedriver"))
        try:
            # 打开目标 URL
            driver.get(self.config.get("url"))
            # 执行一些 UI 操作
            for action in self.config.get("actions", []):
                if "click" in action:
                    element = driver.find_element(By.CSS_SELECTOR, action["click"])
                    element.click()
                    logger.info(f"Clicked on element: {action['click']}")
                elif "type" in action:
                    element = driver.find_element(By.CSS_SELECTOR, action["type"])
                    element.send_keys(action["text"])
                    logger.info(f"Typed text in element: {action['type']}")
                elif "wait_for" in action:
                    element = driver.find_element(By.CSS_SELECTOR, action["wait_for"])
                    logger.info(f"Waited for element: {action['wait_for']}")
            self.result = "UI Test Completed"
            logger.info(f"UI test passed for Job: {self.name}")

        except Exception as e:
            self.status = 'failed'
            logger.error(f"UI test failed with error: {e}")

        finally:
            driver.quit()   # 退出浏览器
            self.persist_result()   # 保存执行结果

