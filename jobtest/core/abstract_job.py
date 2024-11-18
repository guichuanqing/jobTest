# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/18 17:32
# @File : abstract_job.py
# Description : 文件说明
"""
from jobtest.core.job import Job
from jobtest.utils.logger import Logger

logger = Logger().get_logger()

class AbstractJob(Job):
    """Abstract class for intermediate Jobs between root and leaf Jobs."""
    def __init__(self, name: str):
        super().__init__(name)

    def validate(self):
        """验证 Job 的输入和配置是否正确"""
        if not self.input_data:
            raise ValueError(f"Input data is required for Job:{self.name}")

    def execute_dependencies(self):
        """运行所有依赖的 Job"""
        results = {}
        for job in self.dependency:
            logger.info(f"Executing dependency: {job.name}")
            results.append(job.run())
        return all(results)
