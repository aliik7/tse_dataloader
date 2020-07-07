from os import path
import setuptools

directory = path.abspath(path.dirname(__file__))

with open(path.join(directory, "README.md")) as f:
    long_description = f.read()

setuptools.setup(
    name="tse_dataloader",
    version="0.1.1",
    author="Aliik7",
    author_email="aliik2@gmail.com",
    description="Python package for downloading Tehran Stock Exchange data and analysing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aliik7/tse_dataloader",
    packages=setuptools.find_packages(),
    install_requires=["matplotlib", "pandas", "bs4", "requests", "jdatetime"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


