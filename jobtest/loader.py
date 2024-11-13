# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/13 10:11
# @File : loader.py
# Description : 文件说明
"""
from jobtest.utils.config_loader import load_config

# 加载配置文件
config = load_config()
log_level = config.get('log_level')
db_config = config.get('database')

print(f'Log level: {log_level}')
print(f'Database config: {db_config}')