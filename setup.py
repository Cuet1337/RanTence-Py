import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rantence-Cryptos", # Replace with your own username
    version="0.0.1",
    author="Cryptos & Cuet",
    author_email="jenkzzjenkzz@protonmail.com",
    description="A Python package that allows you to generated 1/3 different statements.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cryptos1337/RanTence-Py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
