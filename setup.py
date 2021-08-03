
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:08:30 2021

@author: map
"""
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

datadir = os.path.join('BibleLM','Bible_model_ckpts')
datafiles = [(d, [os.path.join(d,f) for f in files])    for d, folders, files in os.walk(datadir)]
datadir = os.path.join('BibleLM','input_files')
datafiles+= [(d, [os.path.join(d,f) for f in files])    for d, folders, files in os.walk(datadir)]

setuptools.setup(
    name="Bible language model", # 이 패키지를 설치/삭제할 때 사용할 이름을 의미한다. 이 이름과 import할 때 쓰이는 이름은 다르다.
    version="2.0.1",
    author="Hosu Lee",
    author_email="leehosu01@naver.com",
    description="gpt2-medium based bible language model.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leehosu01/BibleLM",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=requirements,
    data_files = datafiles
)