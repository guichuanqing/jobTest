# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/11 18:46
# @File : base_job.py
# Description : 文件说明
"""
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class BaseJob:
    """
    Job 基类，定义 Job 的基础属性和执行流程，符合微测试 Job 模型
    """
    def __init__(self, name: str, config: Dict = None, input_data: Any = None):
        """
        初始化 Job 基类
        :param name: Job 名称
        :param config: Job 配置
        :param input_data: Job 输入数据
        """
        self.name = name
        self.config = config if config else {}
        self.input_data = input_data        # 输入数据
        self.output_data = None             # 输出数据
        self.dao = None                     # 数据持久化
        self.dependency = None              # 前置条件
        self.test_data = None               # 测试数据
        self.test_config = None             # 运行时配置
        self.document = None                # 任务描述和附加信息
        self.status = "initialized"         # Job 的状态（initialized, running, finished, failed）
        self.result = None                  # 执行结果

    def setup(self):
        """前置处理：用于执行 Job 执行前的准备工作。"""
        logger.info(f"Setting up Job: {self.name} ")
        self.status = "running"
        self.validate()

    def execute(self):
        """执行任务：核心的执行逻辑。该方法应该被子类重写，实现具体的任务执行逻辑。"""
        raise NotImplementedError("Subclasses must implement the 'execute' method.")

    def teardown(self):
        """后置处理：用于执行 Job 执行后的清理工作。"""
        logger.info(f"Tearing down Job: {self.name} ")
        self.status = "finished"
        self.persist_result()

    def validate(self):
        """检验配置和环境是否准备好。"""
        if not self.config:
            logger.warning(f"Job {self.name} is missing configuration.")
            self.status = "failed"
            return False
        return True

    def persist_result(self):
        """持久化结果：根据 DAO 属性决定如何保存执行结果"""
        if self.dao:
            logger.info(f"Persisting results for DAO: {self.DAO}")
            # 这里可以根据实际需求保存日志、结果等
            pass

    def run(self):
        """运行整个 Job 流程：包含 setup, execute 和 teardown。"""
        self.setup()
        try:
            self.execute()
            self.status = "finished"
        except Exception as e:
            self.status = "failed"
            logger.error(f"Job {self.name} failed during execution:{e}")
        finally:
            self.teardown()

    def get_result(self):
        """获取 Job 的执行结果。"""
        return self.result