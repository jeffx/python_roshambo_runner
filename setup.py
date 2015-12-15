#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pip.req import parse_requirements
from pip.download import PipSession
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as changelog_file:
    changelog = changelog_file.read()


def get_requirements(filepath):
    analysis = parse_requirements(filepath, session=PipSession())
    return [str(requirement.req) for requirement in analysis]

requirements = get_requirements('requirements.txt')
test_requirements = get_requirements('testing_requirements.txt')

setup(
    name='python_roshambo_runner',
    version='0.1.0',
    description="An Engine that rupits RoShamBo bots against each other",
    long_description=readme + '\n\n' + changelog,
    author="Jeffery Tillotson",
    author_email='jeffx@jeffx.com',
    url='http://sdlc.devcentral.equifax.com/stash/users/jxt131/repos/python_roshambo_runner/python_roshambo_runner',
    packages=[
        'python_roshambo_runner',
    ],
    package_dir={'python_roshambo_runner':
                 'python_roshambo_runner'},
    include_package_data=True,
    install_requires=requirements,
    license="GPLv3",
    zip_safe=False,
    keywords='python_roshambo_runner',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
