# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/18 17:45
# @File : leaf_job.py
# Description : 文件说明
"""
from jobtest.core.abstract_job import AbstractJob
from jobtest.utils.logger import Logger


logger = Logger().get_logger()


class LeafJob(AbstractJob):
    """Final class for leaf Jobs. Represents the actual executable tasks."""

    def __init__(self, name: str, task_function):
        super().__init__(name)
        self.task_function = task_function          # 具体的执行函数

    def run(self):
        """运行 Job 的具体逻辑"""
        self.validate()                     # 验证输入和配置
        logger.info(f"Running Job: {self.name} with input: {self.input_data}")
        if not self.execute_dependencies():
            logger.info(f"Dependency failed for Job: {self.name}")
            return False
        self.output_data = self.task_function(self.input_data)
        logger.info(f"Job {self.name} completed with output: {self.output_data}")
        return True


