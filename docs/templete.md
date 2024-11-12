## ☘️Introduction

此目录用于**存放 & 编辑** seldom 相关文档

## 📖 Document

[中文文档](https://seldomqa.github.io/)

[English document(readthedocs)](https://seldomqa.readthedocs.io/en/latest/index.html)

## 结构

```shell
/project_name
  ├── config/
  │   ├── config.yaml    # 配置文件
  ├── jobs/
  │   ├── example_job.py # 示例 Job 脚本
  ├── logs/
  │   ├── log.txt        # 日志文件
  ├── tests/
  │   ├── test_example.py # 示例测试文件
  ├── cli.py             # CLI 脚本入口
  ├── requirements.txt   # 项目依赖
  └── README.md          # 项目说明文件
```

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