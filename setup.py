#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='i3asap',
    version='0.1.0',
    description="auto setup kali linux i3 desktop",
    long_description=readme + '\n\n' + history,
    author="Steve Tabernacle",
    author_email='stevetabernacle@users.noreply.github.com',
    url='https://github.com/stevetabernacle/i3asap',
    packages=[
        'i3asap',
    ],
    package_dir={'i3asap':
                 'i3asap'},
    entry_points={
        'console_scripts': [
            'i3asap=i3asap.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='i3asap',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
