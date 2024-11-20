# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/11 18:46
# @File : job.py
# Description : 文件说明
"""
from jobtest.utils.logger import Logger
from typing import Dict, List, Optional, Any
from enum import Enum


logger = Logger().get_logger()

class JobStatus(Enum):
    """定义 Job 的运行状态"""
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"


class Job:
    """
    Job 基类，定义 Job 的基础属性和执行流程，支持输入、输出、依赖关系、测试数据和配置等
    """
    def __init__(self,
        job_id: str,
        level: int = 0,
        document: Optional[Any] = None,
        input_data: Optional[Any] = None,
        output_data: Optional[Any] = None,
        dependencies: Optional[List["Job"]] = None,
        test_data: Optional[Dict] = None,
        test_config: Optional[Dict] = None,):
        """
        初始化 Job 基类
        :param name: Job 名称
        :param config: Job 配置
        :param input_data: Job 输入数据
        """
        self.job_id = job_id                    # Job 唯一标识符
        self.level = level                      # Job 层级
        self.input_data = input_data            # 输入数据
        self.output_data = output_data          # 输出数据
        self.dao = None                         # 数据持久化
        self.dependencies: List[Job] = []       # 前置依赖的 Job
        self.test_data = test_data or {}        # 测试数据
        self.test_config = test_config or {}    # 测试配置
        self.document = document or {}          # 任务描述
        self.job_name = None                    # Job 名称
        self.status = JobStatus.PENDING         # 初始状态
        self.children: List[Job] = []           # 子 Job 列表

    def add_child(self, child_job: "Job"):
        """为当前Job添加子Job"""
        child_job.level = self.level + 1        # 子 Job 的层级是当前 Job 的层级加 1
        self.children.append(child_job)

    def inherit_properties(self):
        """子Job继承父Job的属性，除非覆盖"""
        for child in self.children:
            child.test_config = {**self.test_config, **child.test_config}
            child.test_data = {**self.test_data, **child.test_data}

    def run(self):
        """执行 Job，1. 确保所有子 Job 成功运行。2. 汇总子 Job 的运行结果。"""
        self.status = JobStatus.RUNNING
        self.inherit_properties()

        # 运行子Job
        for child in self.children:
            if child.status == JobStatus.PENDING:
                child.run()

        # 检查子Job的运行状态
        if all(child.status == JobStatus.SUCCESS for child in self.children):
            self.status = JobStatus.SUCCESS
            self.output_data = f"{self.job_id} completed successfully."
        else:
            self.status = JobStatus.FAILURE
            self.output_data = f"{self.job_id} failed due to child Job Failure."

    def __repr__(self):
        return f"<Job {self.job_id} ({self.status.value})>"


    # def set_input(self, data):
    #     """设置输入数据"""
    #     self.input_data = data
    #
    # def get_output(self):
    #     """设置输出数据"""
    #     return self.output_data
    #
    # def add_dependency(self, job):
    #     """"添加依赖job"""
    #     self.dependency.append(job)
    #
    # def set_test_data(self, data):
    #     """设置测试数据"""
    #     self.test_data = data
    #
    # def set_config(self, config):
    #     """设置配置"""
    #     self.config.update(config)
    #
    # def set_dao(self, dao):
    #     """设置DAO"""
    #     self.dao = dao
    #
    # def set_document(self, document):
    #     """设置文档信息"""
    #     self.document = document

    # def persist_result(self):
    #     """持久化结果：根据 DAO 属性决定如何保存执行结果"""
    #     if self.dao:
    #         logger.info(f"Persisting results for DAO: {self.DAO}")
    #         # 这里可以根据实际需求保存日志、结果等
    #         pass

if __name__ == "__main__":
    # 定义基础Job
    root_job = Job(job_id="root")
    child_job_1 = Job(job_id="child1")
    child_job_2 = Job(job_id="child2")

    # 添加子Job
    root_job.add_child(child_job_1)
    root_job.add_child(child_job_2)

    # 设置子Job的状态模拟运行结果
    child_job_1.status = JobStatus.FAILURE
    child_job_2.status = JobStatus.SUCCESS

    root_job.run()
    print(root_job)
    print(child_job_1)
    print(child_job_2)
