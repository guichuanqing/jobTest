# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/13 10:11
# @File : loader.py
# Description : 文件说明
"""
from jobtest.utils.config_loader import load_config
import logging

# 加载配置文件
config = load_config()

def get_log_level():
    # 从配置中提取日志级别，默认为 INFO
    return config.get("log_level", "INFO").upper()

def get_db_config():
    db_config = config.get('database')

