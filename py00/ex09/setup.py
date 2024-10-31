from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    long_description=open('README.md').read(),
    author="Semiha Beyazkilic",
    author_email="seozcan@student.42.com",
    url="https://github.com/semx2a/piscine-python/tree/main/py00/ex09",
    packages=find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS independent",
    ],
    python_requires=">=3.6, <4",
)
