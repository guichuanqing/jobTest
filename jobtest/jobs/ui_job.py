# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/14 10:56
# @File : ui_job.py
# Description : 文件说明
"""
from jobtest.utils.logger import Logger
from typing import Dict, Any
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  # selenium>4.0.0
from jobtest.jobs.base_job import BaseJob
import os

logger = Logger().get_logger()


class UiJob(BaseJob):
    """UI 测试任务，继承自 BaseJob，执行 UI 测试逻辑。"""
    def __init__(self, name: str, config: Dict = None, input_data: Any = None):
        super().__init__(name, config, input_data)
        self.level = "ui"    # 定义该 Job 属于 UI 测试层级
        self.driver = None
        # service = Service(executable_path="D:\\ProgramData\\Anaconda3\\Scripts\\chromedriver.exe")
        # # service = Service(executable_path=driver_path)
        # self.driver = webdriver.Chrome(service=service)  # 如果使用 Chrome 浏览器


    def execute(self):
        """执行 UI 测试，模拟用户在浏览器中的交互行为。"""
        logger.info(f"Running UI test for Job: {self.name}")
        driver_path = self.config.get("driver_path", None)
        if not driver_path:
            logger.error("Driver path not specified in config.")
            raise ValueError("Driver path not found in configuration.")
        elif not os.path.exists(driver_path):
            logger.error(f"Chromedriver not found at {driver_path}")
            raise FileNotFoundError(f"Chromedriver not found at {driver_path}")
        logger.info(f"Initializing WebDriver with path: {driver_path}")
        try:
            service = Service(executable_path=driver_path)
            self.driver = webdriver.Chrome(service=service)  # 如果使用 Chrome 浏览器
            try:
                # 打开目标 URL
                self.driver.get(self.config.get("url"))
                # 执行一些 UI 操作
                for action in self.config.get("actions", []):
                    if "click" in action:
                        element = self.driver.find_element(By.CSS_SELECTOR, action["click"])
                        element.click()
                        logger.info(f"Clicked on element: {action['click']}")
                    elif "type" in action:
                        element = self.driver.find_element(By.CSS_SELECTOR, action["type"])
                        element.send_keys(action["text"])
                        logger.info(f"Typed text in element: {action['type']}")
                    elif "wait_for" in action:
                        element = self.driver.find_element(By.CSS_SELECTOR, action["wait_for"])
                        logger.info(f"Waited for element: {action['wait_for']}")
                self.status = 'finished'
                self.result = "UI Test Completed"
                logger.info(f"UI test passed for Job: {self.name}")

            except Exception as e:
                self.status = 'failed'
                logger.error(f"UI test failed with error: {e}")

            finally:
                self.driver.quit()  # 退出浏览器
                logger.info(f"quit driver______________")
        except Exception as e:
            self.status = 'failed'
            logger.error(f"UI test failed with error: {e}")
        finally:
            logger.info(f"quit test______________")
            self.persist_result()   # 保存执行结果



