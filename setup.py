# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_client"
VERSION = "1.2.0"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="",
    author_email="Michael Ward <@devoperandi>",
    url="https://github.com/mward29/python-k8sclient-autoscaling-v1",
    keywords=["Swagger", "python", "client", "kubernetes"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\ This is a python client for Kubernetes Autoscaling v1

    """
)
