# -*- coding: utf-8 -*-
"""
# @Author : qgc
# @Time : 2024/11/11 18:46
# @File : base_job.py
# Description : 文件说明
"""
import click
from jobtest.cli.init_project import init_project

@click.group()
@click.version_option(version='0.1.0', prog_name='jobtest')
@click.option('--log-level', default='INFO', help='Set log level (default: INFO)')
def cli(log_level):
    """
    JobTest - A flexible, job-based testing framework
    """
    click.echo(f"Starting Jobtest with log level:{log_level}")

@cli.command()
@click.argument('path', default='.')
def startproject(path):
    """
    Create a scaffold project with required directories and files.
    """
    click.echo(f"Creating a new JobTest project at {path}")
    # Code to initialize project directories and files goes here


@cli.command()
@click.argument('job_file')
@click.option('--env', default='default', help='Specify environment config')
@click.option('--output', default='./logs', help='Specify output directory for results')
def run(job_file, env, output):
    """
    Run the specified job file.
    """
    click.echo(f"Running job file: {job_file} with enviroment:{env}")
    click.echo(f"Result will be saved to:{output}")
    # Code to load job, execute, and save results goes here

@cli.command()
@click.argument('socurce_format')
@click.argument('target_format')
@click.option('--output', default='./converted', help="Specify output directory for converted files")
def convert(socurce_format, target_format, output):
    """
    Convert job files from one format to another.
    """
    click.echo(f"Converting job files from {socurce_format} to {target_format}")
    click.echo(f"Converted files will be saved to:{output}")
    # Code to convert files goes here

@cli.command()
def help():
    """
    Display help information for JobTest commands.
    """
    click.echo(cli.get_help(click.Context(cli)))

@cli.command()
def version():
    """
    Display the current version of JobTest.
    """
    click.echo("JobTest version 0.1.0")

# register init_project commands
cli.add_command(init_project)

if __name__ == '__main__':
    cli()