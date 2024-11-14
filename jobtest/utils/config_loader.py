# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/13 9:55
# @File : config_loader.py
# Description : 文件说明
"""
import os
import yaml
import logging
from typing import Dict
from pathlib import Path

# 默认配置文件路径
DEFAULT_CONFIG_PATH = 'jobtest/config/default.yaml'

# 环境配置文件路径
ENV_CONFIG_DIR = 'jobtest/config/env'

# 环境变量
ENV_VAR = 'ENV'

# 设置日志记录
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_project_root() -> Path:
    """获取项目根目录"""
    return Path(__file__).parent.parent.parent
def load_config() -> Dict:
    """
    加载配置文件，支持环境变量配置
    按照环境优先级加载配置，先加载 default.yaml，再加载环境特定的配置文件

    返回一个字典，包含所有配置项
    """
    # 获取项目根目录
    project_root = get_project_root()
    # 获取当前环境
    current_env = os.getenv(ENV_VAR, 'dev').lower()
    logger.info(f"Loading configuration for environment: {current_env}")
    # 加载默认配置
    default_config_path = project_root / DEFAULT_CONFIG_PATH
    config = _load_yaml_file(default_config_path)
    # 加载环境特定的配置(如果存在)
    env_config_path = project_root / ENV_CONFIG_DIR / f'{current_env}.yaml'
    if env_config_path.exists():
        logger.info(f"Loading environment-specific configuration: {env_config_path}")
        env_config = _load_yaml_file(env_config_path)
        # 将环境特定的配置合并到默认配置中，后者覆盖前者
        config.update(env_config)
    else:
        logger.warning(f"No environment-specific configuration found for environment: {current_env}")
    return config


def _load_yaml_file(file_path: str) -> Dict:
    """读取并解析YAML配置文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file) or {}
    except Exception as e:
        logger.error(f"Error loading config file '{file_path}': {e}")
        raise RuntimeError(f"Error loading config file '{file_path}': {e}")