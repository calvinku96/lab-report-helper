"""Setup"""
from setuptools import setup

def readme():
    """returns readme string
    """
    with open('README.md') as f:
        return f.read()

setup(
    name='labreporthelper',
    version='0.2.2',
    description='Collection of shortcut methods commonly used to generate plots and tables in lab reports',
    url='https://github.com/calvinku96/labreporthelper',
    author='Calvin',
    author_email='calvinku96@gmail.com',
    license='MIT',
    packages=['labreporthelper', 'labreporthelper.bestfit'],
    install_requires=[
        'numpy', 'scipy', 'matplotlib', 'importlib'
    ],
    scripts=['bin/make-lab-report'],
    zip_safe=False)
