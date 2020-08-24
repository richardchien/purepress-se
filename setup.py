from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="PurePress",
    version="0.1.0",
    url="https://github.com/richardchine/purepress",
    license="MIT License",
    author="Richard Chien",
    author_email="richardchienthebest@gmail.com",
    description="A simple static blog generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(include=("purepress", "purepress.*")),
    install_requires=["Flask", "Markdown", "py-gfm", "PyYAML"],
    python_requires=">=3.7",
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
