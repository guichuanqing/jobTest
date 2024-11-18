# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/11 18:46
# @File : job.py
# Description : 文件说明
"""
from jobtest.utils.logger import Logger
from typing import Dict, Any

logger = Logger().get_logger()

class Job:
    """
    Job 基类，定义 Job 的基础属性和执行流程，符合微测试 Job 模型
    """
    def __init__(self, name: str):
        """
        初始化 Job 基类
        :param name: Job 名称
        :param config: Job 配置
        :param input_data: Job 输入数据
        """
        self.name = name
        self.config = config if config else {}
        self.input_data = None        # 输入数据
        self.output_data = None             # 输出数据
        self.dao = None                     # 数据持久化
        self.dependency = []              # 前置条件
        self.test_data = []               # 测试数据
        self.test_config = {}             # 运行时配置
        self.document = None                # 任务描述和附加信息
        self.status = "initialized"         # Job 的状态（initialized, running, finished, failed）
        self.result = None                  # 执行结果

    def set_input(self, data):
        """设置输入数据"""
        self.input_data = data

    def get_output(self):
        """设置输出数据"""
        return self.output_data

    def add_dependency(self, job):
        """"添加依赖job"""
        self.dependency.append(job)

    def set_test_data(self, data):
        """设置测试数据"""
        self.test_data = data

    def set_config(self, config):
        """设置配置"""
        self.config.update(config)

    def set_dao(self, dao):
        """设置DAO"""
        self.dao = dao

    def set_document(self, document):
        """设置文档信息"""
        self.document = document

    def run(self):
        """执行 Job，子类需要重写此方法"""
        raise NotImplementedError("Subclasses must implement this method.")

    def persist_result(self):
        """持久化结果：根据 DAO 属性决定如何保存执行结果"""
        if self.dao:
            logger.info(f"Persisting results for DAO: {self.DAO}")
            # 这里可以根据实际需求保存日志、结果等
            pass


