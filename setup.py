import setuptools

with open("README.md","r",encoding="utf-8") as fh:
    long_description=fh.read()

setuptools.setup(
    name="pymang",
    version="0.0.1",
    author="Gum Chris",
    author_email="gumchris46@gmail.com",
    description="A simple file managing package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language::Python::3",
        "License::OSI Approved::MIT License",
        "Operating System ::OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6"
)