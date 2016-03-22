"""Setup"""
from setuptools import setup

def readme():
    """returns readme string
    """
    with open('README.md') as f:
        return f.read()

setup(
    name='lab-report-helper',
    version='0.1',
    description='lab-report-helper',
    url='https://github.com/calvinku96/lab-report-helper',
    author='Calvin',
    author_email='calvinku96@gmail.com',
    license='MIT',
    packages=['lab-report-helper'],
    install_requires=[
        'numpy', 'scipy', 'matplotlib', 'importlib'
    ],
    scripts=['bin/make-lab-report'],
    zip_safe=False)
