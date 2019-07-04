from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="easy_tools",
    version="3.3",
    author="Jayanth Sai",
    long_description=long_description,
    author_email="jayanthsai1998@gmail.com",
    description="More routines for operating on iterables and data structures, beyond itertools",
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
