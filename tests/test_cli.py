# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/12 11:28
# @File : test_cli.py
# Description : 文件说明
"""
from click.testing import CliRunner
from jobtest.cli.cli_main import cli

runner = CliRunner()

def test_cli_version():
    result = runner.invoke(cli, ['--version'])
    assert result.exit_code == 0
    assert '0.1.0' in result.output

def test_cli_log_level():
    result = runner.invoke(cli, ['--log-level', 'DEBUG', 'startproject'])
    assert result.exit_code == 0
    assert 'DEBUG' in result.output

def test_startproject_default():
    result = runner.invoke(cli, ['startproject'])
    assert result.exit_code == 0
    assert "Creating a new JobTest project" in result.output

def test_startproject_with_path():
    result = runner.invoke(cli, ['startproject', '/core'])
    assert result.exit_code == 0
    assert "Creating a new JobTest project" in result.output
    assert "/core" in result.output

def test_run_with_defaults():
    result = runner.invoke(cli, ['run', 'job_file.yml'])
    assert result.exit_code == 0
    assert "Running job file: job_file.yml with enviroment:" in result.output
    assert "Result will be saved to:" in result.output

def test_run_with_options():
    result = runner.invoke(cli, ['run', 'job_file.yml', '--env', 'dev', '--output', '/logs'])
    assert result.exit_code == 0
    assert "Running job file: job_file.yml with enviroment:" in result.output
    assert "Result will be saved to:" in result.output

def test_convert():
    result = runner.invoke(cli, ['convert', 'input.yml', 'output.json'])
    assert result.exit_code == 0
    assert "Converting job files from input.yml to output.json" in result.output

def test_help_command():
    result = runner.invoke(cli, ['help'])
    assert result.exit_code == 0
    assert "Usage:  [OPTIONS] COMMAND [ARGS]..." in result.output
    assert "Options:" in result.output
