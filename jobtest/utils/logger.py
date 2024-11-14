# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/14 18:08
# @File : logger.py
# Description : 文件说明
"""
import os
import logging
from logging.handlers import RotatingFileHandler
from jobtest.utils.config_loader import load_config


class Logger:
    """Logger class to manage the logging setup, including console and file logging."""
    def __init__(self):
        """初始化日志配置，支持从配置文件中获取日志级别和输出方式。"""
        self.config = load_config()                      # 加载配置
        self.logger = logging.getLogger(__name__)       # 获取日志记录器实例
        self._set_log_level()                          # 设置日志级别
        self._setup_handlers()                           # 设置日志处理器

    def _set_log_level(self):
        """设置日志级别，默认为 INFO，可以通过配置文件动态调整。"""
        log_level = self.config.get("log_level", "INFO")     # 从配置中读取日志级别
        self.logger.setLevel(log_level)             # 设置日志记录器的日志级别

    def _setup_handlers(self):
        """设置日志处理器，将日志输出到控制台和文件。"""
        # 控制台输出处理器
        ch = logging.StreamHandler()
        ch.setLevel(self.logger.level)
        ch.setFormatter(self._get_log_formatter())
        self.logger.addHandler(ch)

        # 文件日志处理器（支持日志文件滚动）
        log_dir = self.config.get("log_dir", "./logs")   # 配置文件中指定日志目录
        os.makedirs(log_dir, exist_ok=True)              # 如果日志目录不存在，创建它
        log_file = os.path.join(log_dir, "jobtest.log")

        # 设置最大日志文件大小为 10MB，最多保持 5 个日志文件
        fh = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5)
        fh.setLevel(self.logger.level)
        fh.setFormatter(self._get_log_formatter())
        self.logger.addHandler(fh)

    def _get_log_formatter(self):
        """返回一个日志格式化器对象，定义日志输出格式。"""
        return logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        """返回 logger 实例，供外部使用。"""
        return self.logger