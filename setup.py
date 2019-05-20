from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="easy_tools",
    version="0.9",
    author="Jayanth Sai",
    long_description=long_description,
    author_email="jayanthsai1998@gmail.com",
    description="easy_tools is a package that helps to perform operations on iterables or datatypes with less time complexity",
    url="https://github.com/jayanthsai1998/EasyTools",
    license='MIT',
    packages=['easy_tools'],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)
