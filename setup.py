# -*- coding: utf-8 -*-
from os.path import join
import re

from setuptools import setup, find_packages



# dynamically pull the version from djace_editor/__init__.py
version = re.search('^__version__ = "(.+?)"$',
                    open(join('djace_editor', '__init__.py')).read(), re.MULTILINE).group(1)

setup(
    name='djace_editor',
    version=version,
    description='djace_editor provides integration for ajax.org ACE with Django',
    long_description=open('README.rst').read(),

    author='Alex Vakhitov',
    author_email='alex.vakhitov@gmail.com',
    license="Simplified BSD",
    url='https://github.com/smidth/django-ace-editor',

    packages=find_packages(exclude=["example", "example.*"]),
    include_package_data=True,
    install_requires=['Django'],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)