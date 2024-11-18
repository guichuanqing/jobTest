# jobTest
## ☘️Introduction

此目录用于**存放 & 编辑** seldom 相关文档

## 📖 Document

[中文文档](https://seldomqa.github.io/)

[English document(readthedocs)](https://seldomqa.readthedocs.io/en/latest/index.html)

## 结构

```shell
1. 框架整体目录结构
markdown
复制代码
jobtest/
├──docs
├──jobtest/
│   ├──  cli/
│   │     ├── __init__.py
│   │     ├── cli_main.py
│   │     ├── init_project.py
│   ├── config/
│   │     ├── env/
│   │     ├── default.yaml
│   ├── core/
│   │     ├── __init__.py
│   │     ├── job.py
│   │     ├── job_config.py
│   │     ├── job_runner.py
│   │     ├── job_dependency.py
│   │     ├── test_job.py
│   │     ├── leaf_job.py
│   │     ├── abstract_job.py
│   │     ├── test_config.py
│   │     ├── test_data.py
│   ├── utils/
│   │     ├── __init__.py
│   │     ├── logger.py
│   │     ├── json_parser.py
│   │     ├── config_loader.py
│   │     ├── dependency_resolver.py
│   ├── reports/
│   ├── integrations/
│   │     ├── __init__.py
│   │     ├── selenium_integration.py
│   │     ├── Appium_integration.py
│   │     ├── Jemter_integration.py
│   ├── schemas/
│   │     ├── __init__.py
│   │     ├── job_schema.json
│   │     ├── java_test_job_schema.yaml
│   │     ├── selenium_test_job_schema.xml
│   ├── plugins/
├──logs
├──templates
│   ├── job_tempalate.yaml
├──tests
│   ├── __init__.py
│   ├── test_job_execution.py
│   └── test_configuration.py
└── README.md
2. 各目录功能划分
docs/是框架相关说明文档

jobtest/下是主目录文件

cli/目录是命令行相关命令
——cli_main.py是项目支持命令行
——init_project.py是初始化项目脚手架文件

config/目录是全局的配置文件
——env/是多环境配置目录，支持多环境配置
——default.yaml是默认的配置文件，比如日志级别，日志与报告存放路径等

core/ 目录包含框架的核心功能，包括 Job 的定义、配置管理、执行器、 Job 之间的依赖关系处理、以及具体的 Job 实现，包括不同类型的 Job（根 Job、子 Job 和叶子 Job）。
——job.py：定义基础的 Job 类及其接口（如 run()），是所有 Job 类型的父类。
——job_config.py：管理 Job 配置，如 TestConfig，可以定义一些通用配置项，如日志级别、超时等。
——job_runner.py：负责执行整个 Job 流程的调度和管理。它会根据 Job 之间的依赖关系来顺序或并行执行 Job。
——job_dependency.py：处理 Job 之间的依赖关系，确保父 Job 只有在子 Job 成功执行后才能继续执行。
——test_job.py：定义具体的测试任务 Job 类，继承自 AbstractJob，实现 run() 方法。这个类代表一个具体的测试任务。
——leaf_job.py：定义叶子 Job，继承 TestJob 类，最终执行具体的测试操作。
——abstract_job.py：定义抽象 Job 类，作为根 Job 和子 Job 的父类。包含基础的输入输出、配置、依赖等属性。
——test_config.py：定义测试配置类 TestConfig，包括日志级别、超时等设置。
——test_data.py：定义测试数据类，负责存储和传递测试数据。
utils/目录包含一些辅助工具函数和类，帮助框架的其他部分更好地工作。
——logger.py：定义通用的日志框架，包括类别，颜色，格式化等
——config_loader.py：解析默认配置
——xml_parser.py：负责解析 XML 配置文件，加载测试的 Job 配置信息和结构，支持从 XSD 文件验证配置。
——dependency_resolver.py：负责解析并解决 Job 之间的依赖关系，确保按照正确的顺序执行 Job。

integrations/ 目录包含与第三方工具和框架的集成实现。这里可以将 Selenium、JUnit、HttpRunner 等工具的接口封装成 Job，供微测试框架调用。
——selenium_integration.py：集成 Selenium，用于实现 Web 自动化测试。
——Appium_integration.py：集成 Appium，执行 app自动化测试。
——Jemter_integration.py: 集成 jmeter执行接口性能测试。

schemas/ 目录包含测试框架所使用的所有 XML Schema 文件（XSD），用于定义 Job 配置的结构。
——job_schema.json：定义微测试框架json通用的 Job 配置结构。
——java_test_job_schema.yaml：定义 Java 测试类型yaml的 Job 配置结构。
——selenium_test_job_schema.xml：定义 Selenium 测试类型xml的 Job 配置结构。

templatest/ 目录包含模板目录的yaml配置文件
——job_tempalate.yaml:定义脚手架的相关配置

tests/ 目录包含所有的pytest风格的单元测试和集成测试，确保框架的正确性。
——test_job_execution.py：测试 Job 的执行流程，包括根 Job、子 Job 和叶子 Job 的执行顺序、依赖关系和配置管理。
——test_configuration.py：测试 Job 配置的正确性和加载过程，确保 TestConfig 和 TestData 正确传递。

README.md 包含框架的简要介绍、使用方法以及如何扩展和贡献代码的文档。

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