# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/11 18:46
# @File : job.py
# Description : 文件说明
"""
import click
import os
import shutil


# Project initialization function
def create_project_structure(project_name):
    """
    Create the basic directory structure for a new project.
    """
    project_dir = os.path.join(os.getcwd(), project_name)
    # List of directories to create
    directories = ['core', 'config', 'logs', 'tests']
    # Create directories
    if not os.path.exists(project_dir):
        os.mkdir(project_dir)
        click.echo(f"Project directory '{project_name}' created.")
    else:
        click.echo(f"Directory '{project_name}' already exists!")
        return
    # Create subdirectories
    for dir_name in directories:
        dir_path = os.path.join(project_dir, dir_name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
            click.echo(f"Created directory: {dir_name}")
        else:
            click.echo(f"Directory '{dir_name}' already exists!")
    # Create basic files
    create_basic_files(project_dir)

def create_basic_files(project_dir):
    """Create basic files for the new project."""
    # Requirements file
    requirements = os.path.join(project_dir, 'requirements.txt')
    with open(requirements, 'w') as f:
        f.write("pytest\nclick\n")
    click.echo(f"Created requirements.txt.")
    # Readme file
    readme = os.path.join(project_dir, 'README.md')
    with open(readme, 'w') as f:
        f.write(f"# {os.path.basename(project_dir)}\n\nThis is a test project using the micro-test Job model.")
    click.echo(f"Created README.md.")
    # Example test files
    test_file = os.path.join(project_dir, 'tests', 'test_example.py')
    with open(test_file, 'w') as f:
        f.write("""
import pytest
def test_example():
    assert True
""")
        click.echo(f"Created example test file: tests/test_example.py.")
        # Example job files
        job_file = os.path.join(project_dir, 'core', 'example_job.py')
        with open(job_file, 'w') as f:
            f.write("""
def example_job():
    print("This is an example job.")
""")
        click.echo(f"Created example job file: core/example_job.py.")
        # config.yaml
        config_file = os.path.join(project_dir, 'config', 'config.yaml')
        with open(config_file, 'w') as f:
            f.write("""
log_level: INFO
job_timeout: 60
""")
    click.echo(f"Created configuration file: config/config.yaml.")

# Project initialization command
@click.command()
@click.argument('project_name', type=str)
def init_project(project_name):
    """Initialize a new project with a basic directory structure."""
    try:
        create_project_structure(project_name)
        click.echo(f"Project '{project_name}' initialized successfully!")
    except Exception as e:
        click.echo(f"Error initializing project: {str(e)}")
