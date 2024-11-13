# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/13 10:14
# @File : test_config_loader.py
# Description : 文件说明
"""
import os
import pytest
from jobtest.utils.config_loader import load_config

@pytest.fixture
def set_env_var():
    """Fixture to set the environment variable for testing."""
    original_env = os.getenv('ENV')
    os.environ['ENV'] = 'pro'
    yield
    if original_env is None:
        del os.environ['ENV']
    else:
        os.environ['ENV'] = original_env

def test_load_config(set_env_var):
    """Test loading of config based on environment."""
    config = load_config()

    assert config['log_level'] == 'ERROR'
    assert config['database']['host'] == 'test-db-host'

def test_load_default_config():
    """Test loading of default config when no environment is set."""
    os.environ["ENV"] = 'DEV'
    config = load_config()
    assert config['log_level'] == 'DEBUG'
    assert config['database']['host'] == 'dev-db-host'