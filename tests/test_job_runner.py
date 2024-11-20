# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/20 17:58
# @File : test_job_runner.py
# Description : 文件说明
"""
import pytest
import asyncio
from jobtest.core.job import Job, JobStatus
from jobtest.core.job_runner import JobRunner
from jobtest.utils.logger import Logger



logger = Logger().get_logger()

@pytest.mark.asyncio
async def test_job_execution():
    runner = JobRunner()
    root = Job(job_id="root")
    child1 = Job(job_id="child1")
    child2 = Job(job_id="child2")

    root.add_child(child1)
    root.add_child(child2)

    await runner.run(root)

    assert root.status == JobStatus.SUCCESS
    assert child1.status == JobStatus.SUCCESS
    assert child2.status == JobStatus.SUCCESS

@pytest.mark.asyncio
async def test_job_dependency_execution():
    runner = JobRunner()
    job1 = Job(job_id="job1")
    job2 = Job(job_id="job2")
    job3 = Job(job_id="job3")

    job3.dependencies = [job2]
    job2.dependencies = [job1]

    job1.level = 1
    job2.level = 1
    job3.level = 1

    root = Job(job_id="root")
    root.add_child(job3)
    root.add_child(job2)
    root.add_child(job1)

    await runner.run(root)

    assert job1.status == JobStatus.SUCCESS
    assert job2.status == JobStatus.SUCCESS
    assert job3.status == JobStatus.SUCCESS


@pytest.mark.asyncio
async def test_job_execution_with_failure():
    runner = JobRunner()

    class FailingJob(Job):
        async def run(self):
            raise Exception("Job failed")

    root = Job(job_id="root")
    failing_child = FailingJob(job_id="failing")
    normal_child = Job(job_id="normal")

    root.add_child(failing_child)
    root.add_child(normal_child)

    await runner.run(root)
    assert root.status == JobStatus.FAILURE
    assert failing_child.status == JobStatus.FAILURE
    assert normal_child.status == JobStatus.SUCCESS