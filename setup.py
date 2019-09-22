from setuptools import setup

requirements = ["graphviz"]

setup(
    name="MicroRegEx",
    version="1.0.0",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    packages=[
        "MicroRegEx",
        "MicroRegEx.Lexer",
        "MicroRegEx.Parser",
        "MicroRegEx.Automaton",
        "MicroRegEx.Automaton.Minimal",
        "MicroRegEx.Automaton.SubsetConstruct",
    ],
    install_requires=requirements,
    license="MIT license",
    url="https://github.com/howl-anderson/MicroRegEx",
    author="Xiaoquan Kong",
    author_email="u1mail2me@gmail.com",
    description="A micro regular expression engine",
)
