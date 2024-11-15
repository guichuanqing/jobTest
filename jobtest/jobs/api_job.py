# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/14 10:55
# @File : api_job.py
# Description : 文件说明
"""
import requests
from typing import Dict, Any
from jobtest.jobs.base_job import BaseJob
from jobtest.utils.logger import Logger


logger = Logger().get_logger()

class ApiJob(BaseJob):
    """API 测试任务，继承自 BaseJob，执行 API 测试逻辑。"""
    def __init__(self, name: str, config: Dict = None, input_data: Any = None):
        super().__init__(name, config, input_data)
        self.level = 'api'  # 定义Job属于api测试层级

    def execute(self):
        """执行 API 测试，调用目标 API，并验证响应结果。"""
        logger.info(f"Running API test for Job: {self.name}")
        url = self.config.get("url")
        method = self.config.get("method", "GET")
        payload = self.config.get("payload", {})
        headers = self.config.get("headers", {})

        if not url:
            logger.error("URL not provided in configuration.")
            self.status = "failed"
            return
        try:
            # 根据请求方法执行 API 请求
            if method.upper() == "POST":
                response = requests.post(url, json=payload, headers=headers)
            else:
                response = requests.get(url, json=payload, headers=headers)

            # 检查响应状态
            if response.status_code ==200:
                self.status = "finished"
                self.result = response.json()
                logger.info(f"API test passed. Response: {self.result}")
            else:
                self.status = "failed"
                logger.error(f"API test failed. Status code: {response.status_code}, Response: {response.text}")
        except Exception as e:
            self.status = 'failed'
            logger.error(f"API test failed with error: {e}")

        self.persist_result()   # 保存执行结果