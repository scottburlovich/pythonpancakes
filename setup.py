import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pythonpancakes",
    version="1.0.0",
    description="A basic request wrapper for the PancakeSwap API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/scottburlovich/pythonpancakes",
    author="Scott Burlovich",
    author_email="teedot@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=['pythonpancakes'],
    package_dir={'pythonpancakes': 'src/pythonpancakes'},
    include_package_data=True,
    install_requires=["requests"]
)
