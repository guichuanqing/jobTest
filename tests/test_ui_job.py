# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/14 18:50
# @File : test_ui_job.py
# Description : 文件说明
"""
import pytest
from unittest.mock import patch
from jobtest.jobs.ui_job import UiJob


@pytest.fixture
def ui_job():
    config = {
        "url": "https://www.example.com",
        "driver_path": "/path/to/chromedriver",
        "actions": [
            {"click": "button#submit"},
            {"wait_for": "div#result"}
        ]
    }
    return UiJob(name="Test UI Job", config=config)

def test_ui_job_success(ui_job, caplog):
    """测试 UI 测试成功的情况"""
    # 使用 mock 模拟 WebDriver 的行为
    with patch("selenium.webdriver.Chrome") as mock_driver:
        mock_driver_instance = mock_driver.return_value
        mock_driver_instance.find_element.return_value = mock_driver_instance       # Mock elements
        mock_driver_instance.find_element_by_css_selector.return_value = mock_driver_instance

        ui_job.execute()

        # 验证 Job 的状态
        assert ui_job.status == "finished"
        assert "UI test passed" in caplog.text

def test_ui_job_failure(ui_job, caplog):
    """ 测试 UI 测试失败的情况 """

    # 使用 mock 模拟 WebDriver 的行为，当找不到元素时抛出异常
    with patch("selenium.webdriver.Chrome") as mock_driver:
        mock_driver_instance = mock_driver.return_value
        mock_driver_instance.find_element.side_effect = Exception("Element not found")

        ui_job.execute()

        # 验证 Job 的状态
        assert ui_job.status == "failed"
        assert "UI test failed" in caplog.text  # 检查日志中是否包含失败信息

def test_ui_job_exception(ui_job, caplog):
    """测试 UI 测试时发生异常的情况"""
    # 使用 mock 模拟 WebDriver 抛出异常
    with patch("selenium.webdriver.Chrome") as mock_driver:
        mock_driver.side_effect = Exception("WebDriver initialization failed")

        ui_job.execute()
        # 验证 Job 的状态为失败
        assert ui_job.status == "failed"
        assert "UI test failed with error" in caplog.text  # 检查日志中是否包含错误信息