# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/20 14:28
# @File : job_runner.py
# Description : 文件说明
"""
import asyncio
from typing import List, Dict
from jobtest.core.job import Job, JobStatus
from jobtest.utils.logger import Logger
from jobtest.core.job_dependency import DependencyResolver


logger = Logger().get_logger()

class JobRunner:
    """Job调度器，支持异步执行Job。"""
    def __init__(self):
        self.execution_results: Dict[str, JobStatus] = {}

    async def execute_job(self, job: Job):
        """执行单个Job。"""
        # 如果存在未完成的依赖，等待他们
        # for dependency in job.dependencies:
        #     while dependency.status not in (JobStatus.SUCCESS, JobStatus.FAILURE):
        #         await asyncio.sleep(0.1)
        #
        #     if dependency.status == JobStatus.FAILURE:
        #         job.status = JobStatus.FAILURE
        #         job.output_data = f"Dependency {dependency.job_id} failed."
        #         self.execution_results[job.job_id] = JobStatus.FAILURE
        #         return
        if job.status != JobStatus.PENDING:
            logger.warning(f"Skipping Job {job.job_id} as it is already {job.status.value}.")
            return
        logger.info(f"Starting execution of Job {job.job_id}")
        # 检查依赖是否完成并成功
        if any(dep.status != JobStatus.SUCCESS for dep in job.dependencies):
            job.status = JobStatus.FAILURE
            logger.error(f"Job {job.job_id} failed due to unmet dependencies.")
            return

        # 执行Job
        try:
            await job.run()
            job.status = JobStatus.SUCCESS
            logger.info(f"Job {job.job_id} completed successfully.")
        except Exception as e:
            job.status = JobStatus.FAILURE
            logger.error(f"Job {job.job_id} failed with error: {e}")


    async def execute_children(self, job: Job):
        """并发执行当前Job的所有子Job"""
        tasks = [self.execute_job(child) for child in job.children]
        await asyncio.gather(*tasks)


    async def run(self, root_job: Job):
        """异步运行根Job（包括其所有子Job）。"""
        logger.info(f"Starting execution of root Job: {root_job.job_id}")

        # 收集所有Job
        all_jobs = self.collect_all_jobs(root_job) or []

        # 校验依赖规则
        DependencyResolver.validate_dependencies(all_jobs)

        # 解析执行顺序（分层解析）
        execution_order_by_layers = DependencyResolver.resolve_execution_order_by_layers(all_jobs)

        # 按解析顺序运行 Job
        for layer  in execution_order_by_layers:
            await self.execute_jobs_in_layer(layer)

        logger.info(f"Root Job {root_job.job_id} finished with status {root_job.status.value}.")

    def collect_all_jobs(self, root_job: Job) -> List[Job]:
        """递归收集整个Job树中的所有Job。"""
        if not root_job:
            return []

        all_jobs = []
        stack = [root_job]
        while stack:
            job = stack.pop()
            all_jobs.append(job)
            stack.extend(job.children)
        return all_jobs

    async def execute_jobs_in_layer(self, jobs: List[Job]):
        """并发执行同层的所有Job"""
        tasks = [self.execute_job(job) for job in jobs]
        await asyncio.gather(*tasks, return_exceptions=True)

    def get_execution_result(self) -> Dict[str, JobStatus]:
        """获取所有Job的执行结果"""
        return self.execution_results


# 测试 JobRunner
if __name__ == "__main__":
    # 创建 Job 树
    root_job = Job(job_id="root", )
    child_job_1 = Job(job_id="child1", )
    child_job_2 = Job(job_id="child2", )
    sub_child_job_1 = Job(job_id="sub_child1", )
    sub_child_job_2 = Job(job_id="sub_child2", )

    # 构建 Job 树结构
    root_job.add_child(child_job_1)
    root_job.add_child(child_job_2)
    child_job_1.add_child(sub_child_job_1)
    child_job_1.add_child(sub_child_job_2)

    # 定义依赖关系
    child_job_2.dependencies = [child_job_1]
    sub_child_job_2.dependencies = [sub_child_job_1]
    # try:
    #     sub_child_job_2.dependencies = [child_job_1] # 非法依赖
    # except ValueError as e:
    #     print(e)

    # 运行 Job 调度器
    runner = JobRunner()
    try:
        asyncio.run(runner.run(root_job))
    except ValueError as e:
        print("Dependency validation failed:", e)

    # 输出执行结果
    for job_id, status in runner.get_execution_result().items():
        print(f"Job {job_id} finished with status: {status.value}")