# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='djace_editor',
    version='0.9.1',
    description='djace_editor provides integration for ajax.org ACE with Django',
    long_description=open('README.rst').read(),

    author='Alex Vakhitov',
    author_email='alex.vakhitov@gmail.com',
    license="Simplified BSD",
    url='https://github.com/smidth/django-ace-editor',

    packages=['djace_editor'],
    include_package_data=True,
    install_requires=['Django', 'setuptools'],

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