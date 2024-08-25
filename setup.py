##############################################################################
#
# Copyright (c) 2006-2015 Agendaless Consulting and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the BSD-like license at
# http://www.repoze.org/LICENSE.txt.  A copy of the license should accompany
# this distribution.  THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL
# EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND
# FITNESS FOR A PARTICULAR PURPOSE
#
##############################################################################

import os
import sys

tests_require = []
testing_extras = tests_require + [
    'pytest',
    'pytest-cov',
    ]

from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))
try:
    with open(os.path.join(here, 'README.rst'), 'r') as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGES.rst'), 'r') as f:
        CHANGES = f.read()
except Exception:
    README = """\
Supervisor is a client/server system that allows its users to
control a number of processes on UNIX-like operating systems. """
    CHANGES = ''

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: No Input/Output (Daemon)',
    'Intended Audience :: System Administrators',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Topic :: System :: Boot',
    'Topic :: System :: Monitoring',
    'Topic :: System :: Systems Administration',
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

version_txt = os.path.join(here, 'supervisor/version.txt')
with open(version_txt, 'r') as f:
    supervisor_version = f.read().strip()

dist = setup(
    name='supervisor',
    version=supervisor_version,
    license='BSD-derived (http://www.repoze.org/LICENSE.txt)',
    url='http://supervisord.org/',
    project_urls={
        'Changelog': 'http://supervisord.org/changelog',
        'Documentation': 'http://supervisord.org',
        'Issue Tracker': 'https://github.com/Supervisor/supervisor',
    },
    description="A system for controlling process state under UNIX",
    long_description=README + '\n\n' + CHANGES,
    classifiers=CLASSIFIERS,
    author="Chris McDonough",
    author_email="chrism@plope.com",
    packages=find_packages(),
    extras_require={
        'testing': testing_extras,
    },
    tests_require=tests_require,
    include_package_data=True,
    zip_safe=False,
    test_suite="supervisor.tests",
    entry_points={
        'console_scripts': [
            'supervisord = supervisor.supervisord:main',
            'supervisorctl = supervisor.supervisorctl:main',
            'echo_supervisord_conf = supervisor.confecho:main',
            'pidproxy = supervisor.pidproxy:main',
        ],
    },
)
