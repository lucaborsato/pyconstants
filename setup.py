import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyconstants",
    version="0.0.1",
    author="Luca Borsato",
    author_email="borsato.luca@gmail.com",
    description="Constants package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lucaborsato",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
