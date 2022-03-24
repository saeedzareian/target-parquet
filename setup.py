#!/usr/bin/env python

from setuptools import setup

setup(
    name="target-parquet",
    version="0.2.3",
    description="Singer.io target for writing into parquet files",
    author="Rafael 'Auyer' Passos",
    url="https://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["target_parquet"],
    install_requires=[
        "jsonschema==4.4.0",
        "singer-python==5.12.2",
        "pyarrow==7.0.0",
        "psutil==5.9.0",
    ],
    extras_require={
        'dev': [
            'pytest==6.2.4',
            'pandas==1.4.1'
        ]
    },
    entry_points="""
          [console_scripts]
          target-parquet=target_parquet:main
      """,
    packages=["target_parquet"],
)
