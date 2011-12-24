# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "waxyay",
    version = "1.0",
    url = 'https://github.com/mickymiseck/waxyay',
    license = 'GPL v.3',
    description = "Sistema de administración de afiliados del ****.",
    long_description = read('README'),

    author = 'Miguel Angel Cumpa Asuña',
    author_email = 'themiseck.rock@gmail.com',

    packages = find_packages('src'),
    package_dir = {'': 'src'},

    install_requires = ['setuptools'],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL v.3 License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
