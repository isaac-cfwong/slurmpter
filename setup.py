from setuptools import setup, find_packages

VERSION = "0.1.0"

setup(
    name="slurmpter",
    version=VERSION,
    license="MIT",
    description="A package to build Slurm submit files of a workflow of jobs easily.",
    author="Isaac Chun Fung WONG",
    author_email="chunefung@gmail.com",
    url="https://gitlab.com/isaac-cfwong/slurmpter",
    python_requires=">=3.5",
    packages=find_packages(),
    install_requires=["pycondor"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
