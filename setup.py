#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/11/25 14:54
# @Author  : 三哥
# @Site    : 
# @File    : setup.py
# @Software: PyCharm

from setuptools import setup, find_packages

setup(
    name='typeidea',
    version='0.1',
    description='Blog System base on Django',
    author='sanyue',
    author_email='sanyuedev@gmail.com',
    url='https://sanyuedev.top',
    license='MIT',
    packages=find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    package_data={'': [
        'themes/*/*/*/*'
    ]},
    install_requires=[
        'Django==2.2.7',
        'django-rest-framework==0.1.0',
        'djangorestframework==3.11.2',
        'mistune==0.8.4',
        'pytz==2019.3',
        'sqlparse==0.3.0',

    ],
    scripts=[
        'typeidea/manage.py',
        'typeidea/typeidea/wsgi/py'
    ],
    entry_points={
        'console_scripts': [
            'typeidea_manage = manage:main'
        ]
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ]
)
