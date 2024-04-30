#!/usr/bin/env python3

import setuptools

from pathlib import Path

build = Path(__file__).parent / "build.txt"
def get_build():
    if build.is_file():
        num = int(build.read_text())
        build.write_text(str(num+1))
        return num+1
    else:
        build.write_text("0")
        return 0

setuptools.setup(
    name='xdialog',
    version=f'1.2.0.{get_build()}',
    author='mathgeniuszach',
    author_email='huntingmanzach@gmail.com',
    description='A cross-platform python wrapper for native dialogs.',
    long_description='A cross-platform python wrapper for native dialogs. Portable as it only uses the standard library.',
    url='https://github.com/xMGZx/xdialog',
    packages=['xdialog'],
    license='MIT License',
    classifiers=['Programming Language :: Python :: 3']
)

