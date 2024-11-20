# jobTest
## ☘️Introduction

此目录用于**存放 & 编辑** seldom 相关文档

## 📖 Document

[中文文档](https://seldomqa.github.io/)

[English document(readthedocs)](https://seldomqa.readthedocs.io/en/latest/index.html)

## 结构

```shell
jobtest/
├── docs/                    # 框架说明文档
├── jobtest/                 # 框架主代码目录
│   ├── cli/                 # 命令行工具模块
│   │     ├── __init__.py
│   │     ├── cli_main.py    # 命令行主入口
│   │     ├── init_project.py# 初始化项目脚手架工具
│   ├── config/              # 配置文件和管理模块
│   │     ├── __init__.py
│   │     ├── default.yaml   # 默认配置
│   │     ├── env.yaml       # 环境配置（包含多环境选项）
│   ├── core/                # 核心模块
│   │     ├── __init__.py
│   │     ├── job.py         # 基础 Job 定义（统一抽象和叶子实现）
│   │     ├── job_runner.py  # Job 调度器和执行逻辑
│   │     ├── job_dependency.py # Job 依赖管理
│   │     ├── test_data.py   # 测试数据类
│   │     ├── test_config.py # 测试配置类
│   ├── utils/               # 工具模块
│   │     ├── __init__.py
│   │     ├── logger.py      # 日志工具
│   │     ├── config_loader.py # 配置加载工具
│   │     ├── dependency_resolver.py # 依赖解析工具
│   ├── integrations/        # 集成工具模块
│   │     ├── __init__.py
│   │     ├── selenium_integration.py # Selenium 集成
│   │     ├── appium_integration.py   # Appium 集成
│   │     ├── jmeter_integration.py   # JMeter 集成
│   ├── schemas/             # 配置结构模式（Schema）
│   │     ├── __init__.py
│   │     ├── job_schema.yaml         # Job 通用配置结构
│   │     ├── selenium_job_schema.yaml# Selenium 测试配置
│   ├── plugins/             # 用户自定义插件模块
│   │     ├── __init__.py
│   │     ├── example_plugin.py       # 示例插件
├── logs/                    # 日志存放目录
├── templates/               # 配置模板目录
│   ├── job_template.yaml    # Job 模板
├── tests/                   # 测试目录
│   ├── __init__.py
│   ├── test_core.py         # 核心模块的单元测试
│   ├── test_integrations.py # 集成模块的测试
├── README.md                # 项目简介和使用文档
├── setup.py                 # 项目安装脚本
├── pyproject.toml           # 项目配置文件（依赖管理）
├── requirements.txt         # 依赖列表
└── .pre-commit-config.yaml  # 代码质量工具配置

## 如何贡献文档

1. clone 本项目

```bash
git clone https://github.com/SeldomQA/seldom.git
```

2. 进入到文档目录&启动项目

```bash
cd docs

npm install yarn -g

yarn install

yarn run dev
```

3. 编辑相关文档（推荐编辑 vpdocs 目录下的文档，该目录的文档也是 seldom 的主要文档）

4. push 到 vuepress-docs 分支