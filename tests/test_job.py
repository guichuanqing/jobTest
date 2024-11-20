# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/20 17:24
# @File : test_job.py
# Description : 文件说明
"""
import pytest
from jobtest.core.job import Job, JobStatus

def test_job_creation():
    job = Job(job_id="job1")
    assert job.job_id == "job1"
    assert job.status == JobStatus.PENDING
    assert job.level == 0
    assert job.dependencies ==[]
    assert job.children == []

def test_jon_add_child():
    parent = Job(job_id="parent")
    child = Job(job_id="child")

    parent.add_child(child)
    assert child in parent.children
    assert child.level == parent.level + 1

def test_job_repr():
    job = Job(job_id="job1")
    assert repr(job) == "<Job job1 (PENDING)>"