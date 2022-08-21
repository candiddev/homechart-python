import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    author="Candid Development",
    author_email="support@candid.dev",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description="Python library for interacting with the Homechart API",
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
    name="homechart",
    package_dir={'': 'src'},
    packages=setuptools.find_packages(),
    py_modules=["homechart"],
    python_requires='>=3.9',
    url="https://github.com/candiddev/homechart-python",
    version=os.getenv("BUILD_TAG"),
)
