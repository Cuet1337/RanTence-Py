import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rantence",
    version="6.0.0",
    author="Cryptos & Cuet",
    author_email="jenkzzjenkzz@protonmail.com",
    description="A Python package that allows you to generated 1/3 different statements.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cryptos1337/RanTence-Py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 4",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=['random'],
)
