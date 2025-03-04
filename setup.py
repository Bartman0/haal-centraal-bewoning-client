# coding: utf-8

"""
    BRP bewoning

    API voor het raadplegen van de (historische) bewoning van een adres. 

    The version of the OpenAPI document: 2.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "brp-bewoning-client"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="BRP bewoning",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "BRP bewoning"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="European Union Public License, version 1.2 (EUPL-1.2)",
    long_description_content_type='text/markdown',
    long_description="""\
    API voor het raadplegen van de (historische) bewoning van een adres. 
    """,  # noqa: E501
    package_data={"brp_bewoning_client": ["py.typed"]},
)
