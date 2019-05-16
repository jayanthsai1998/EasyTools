from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="easy_tools",
    version="0.0.1",
    author="Jayanth Sai",
    author_email="jayanthsai1998@gmail.com",
    description="easy_tools is a package that helps to perform easy operations on iterables with less time complexity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jayanthsai1998/EasyTools",
    packages=['easy_tools'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
