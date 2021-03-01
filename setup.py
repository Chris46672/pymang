import setuptools


setuptools.setup(
    name="pymang",
    version="0.0.1",
    author="Gum Chris",
    url="https://github.com/Chris46672/pymang",
    author_email="gumchris46@gmail.com",
    description="A simple file managing package",
    long_description="A python lib",
    long_description_content_type="text/plain",
    include_package_data=True,
    classifiers=[
        "Programming Language::Python::3",
        "License::OSI Approved::MIT License",
        "Operating System ::OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6"
)