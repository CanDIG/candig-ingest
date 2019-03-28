#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "docopt",
    "ga4gh-server",
    "pandas"
]

setup_requirements = [
]

test_requirements = [
]

setup(
    name='ingest',
    version='1.0.0',
    description="Routines for ingesting metadata to a CanDIG repository",
    long_description=readme + '\n\n' + history,
    author="CanDIG team",
    author_email='',
    url='https://github.com/CanDIG/candig-ingest.git',
    packages=find_packages(include=['candig-ingest']),
    namespace_packages=["ga4gh"],
    entry_points={
        'console_scripts': [
            'ingest=ga4gh.ingest.ingest:main'
            'load_tier=ga4gh.ingest.load_tiers:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='candig-ingest',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
    dependency_links=[
     "git+https://github.com/CanDIG/candig-server.git@develop#egg=ga4gh_server"
    ]
)
