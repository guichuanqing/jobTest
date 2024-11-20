# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/20 17:38
# @File : test_job_dependency.py
# Description : 文件说明
"""
import pytest
from jobtest.core.job import Job
from jobtest.core.job_dependency import DependencyResolver



def test_dependency_validation_pass():
    job1 = Job(job_id="job1", level=1)
    job2 = Job(job_id="job2", level=1)
    job1.dependencies = [job2]

    try:
        DependencyResolver.validate_dependencies([job1, job2])
    except ValueError:
        pytest.fail("validate_dependencies raised ValueError unexpectedly!")

def test_dependency_validation_fail():
    job1 = Job(job_id="job1", level=1)
    job2 = Job(job_id="job2", level=2)
    job1.dependencies = [job2]

    with pytest.raises(ValueError) as excinfo:
        DependencyResolver.validate_dependencies([job1, job2])
    assert "Invalid dependency" in str(excinfo.value)


def test_execution_order():
    job1 = Job(job_id="job1")
    job2 = Job(job_id="job2")
    job3 = Job(job_id="job3")
    job2.dependencies = [job1]
    job3.dependencies = [job2]

    order = DependencyResolver.resolve_execution_order([job3, job2, job1])
    assert order == [job1, job2, job3]