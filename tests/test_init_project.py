# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/12 15:27
# @File : test_init_project.py
# Description : 文件说明
"""
import os
import pytest
import shutil
from click.testing import CliRunner
from jobtest.cli.init_project import init_project

@pytest.fixture()
def runner():
    """Create a runner instance to invoke CLI commands."""
    return CliRunner()

@pytest.fixture()
def clean_up_project():
    """Fixture to clean up project directories after test."""
    yield
    # Clean up project directories
    if os.path.exists('test_project'):
        shutil.rmtree('test_project')

def test_init_project(runner, clean_up_project):
    """Test that the 'init_project' CLI command creates the necessary project structure."""
    # Run the 'init_project' command
    result = runner.invoke(init_project, ['test_project'])
    assert result.exit_code == 0
    assert "Project 'test_project' initialized successfully" in result.output

    # Check if the project directories were created
    assert os.path.isdir('test_project/config')
    assert os.path.isdir('test_project/jobs')
    assert os.path.isdir('test_project/logs')
    assert os.path.isdir('test_project/tests')

    # Check if the README.md file was created
    assert os.path.isfile('test_project/README.md')
    with open("test_project/README.md") as f:
        assert "# test_project" in f.read()

    # Check if the requirements.txt file was created
    assert os.path.isfile('test_project/requirements.txt')
    with open("test_project/requirements.txt") as f:
        assert "pytest" in f.read()

    # Check if the config.yaml file was created
    assert os.path.isfile("test_project/config/config.yaml")
    with open("test_project/config/config.yaml", "r") as f:
        assert "log_level: INFO" in f.read()

    # Check if the example job was created
    assert os.path.isfile("test_project/jobs/example_job.py")
    with open("test_project/jobs/example_job.py", "r") as f:
        assert "This is an example job." in f.read()

    # Check if the example test was created
    assert os.path.isfile("test_project/tests/test_example.py")
    with open("test_project/tests/test_example.py", "r") as f:
        assert "def test_example()" in f.read()