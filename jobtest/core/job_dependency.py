# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/20 16:12
# @File : job_dependency.py
# Description : 文件说明
"""
from jobtest.core.job import Job
from jobtest.utils.logger import Logger
from typing import List


logger = Logger().get_logger()

class DependencyResolver:
    """Job 依赖管理器，用于校验和解析 Job 的依赖关系。"""

    @staticmethod
    def validate_dependencies(jobs: List[Job]):
        """校验所有Job的依赖是否符合规则4"""
        if not jobs:
            raise ValueError("The job list provided is empty or None.")

        for job in jobs:
            for dependency in job.dependencies:
                if dependency.level != job.level:
                    raise ValueError(f"Invalid dependency: Job {job.job_id} (level {job.level}) "
                        f"cannot depend on Job {dependency.job_id} (level {dependency.level}).")

    @staticmethod
    def resolve_execution_order_by_layers(jobs: List[Job]) -> List[List[Job]]:
        """解析 Job 的执行顺序，按层级返回 Job 列表。"""
        layers = []
        visited = set()

        def resolver_layer(current_jobs):
            next_layer = []
            for job in current_jobs:
                if job not in visited:
                    visited.add(job)
                    next_layer.extend([child for child in job.children if child not in visited])
            return next_layer
        # 初始层级为没有被任何 Job 依赖的根节点
        current_layer = [job for job in jobs if not any(job in child.dependencies for child in jobs)]
        while current_layer:
            layers.append(current_layer)
            current_layer = resolver_layer(current_layer)

        return layers