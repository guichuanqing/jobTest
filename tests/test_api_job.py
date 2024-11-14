# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/14 11:36
# @File : test_api_job.py
# Description : 文件说明
"""
import pytest
from unittest.mock import patch
from jobtest.jobs.api_job import ApiJob


@pytest.fixture
def api_job():
    config = {
        "url": "https://jsonplaceholder.typicode.com/posts",
        "method": "GET",
        "payload": {},
        "headers": {}
    }
    return ApiJob(name="Test Api Job", config=config)

def test_api_job_success(api_job, caplog):
    """测试 API 请求成功的情况"""
    # 使用 mock 模拟 requests.get 返回的响应
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"id": 1, "title": "foo", "body": "bar"}

        api_job.execute()
        # 验证 Job 的结果是否正确
        assert api_job.status == "finished"
        assert api_job.result == {"id": 1, "title": "foo", "body": "bar"}
        # assert "API test passed" in caplog.text  # 检查日志中是否包含错误信息

def test_api_job_failure(api_job, caplog):
    """ 测试 API 请求失败的情况 """
    # 使用 mock 模拟 requests.get 返回的错误响应
    with patch("requests.get") as mock_get:
        mock_get.return_value.status_code = 404
        mock_get.return_value.text = "Not Found"

        api_job.execute()
        # 验证 Job 的状态为失败
        assert api_job.status == "failed"
        assert "API test failed" in caplog.text

def test_api_job_exception(api_job, caplog):
    """测试 API 请求时出现异常的情况"""
    # 使用 mock 模拟 requests.get 抛出异常
    with patch("requests.get") as mock_get:
        mock_get.side_effect = Exception("Connection Error")

        api_job.execute()
        # 验证 Job 的状态为失败
        assert api_job.status == "failed"
        assert "API test failed with error" in caplog.text