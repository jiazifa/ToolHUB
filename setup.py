from setuptools import setup
import os

HERE = os.path.dirname(__name__)
os
REQUIRED: list = [
    "lxml", "requests", "celery"
]

setup(
    name="tools_backend",
    version="0.1.0",
    packages=REQUIRED,
    include_package_data=True,
    zip_safe=False,
)
