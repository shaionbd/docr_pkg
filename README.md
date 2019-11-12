# docr_pkg
This repo is created as a purpose of pip package

##  Process to create pip package

#### Create a venv for python

```
$ python -m venv venv
```

#### Upgrade and install pip setuptools and wheel

```
$ pip install --upgrade pip setuptools wheel 
```

#### Install Twine (A package to authenticate and verified connection between project and PyPi)

```
$ pip install --user --upgrade twine
```
#### Install TQDM package (Progress meter used internally by Twine)

```
$ pip install tqdm
```

#### Now create a setup.py file which contains all the metadata of projects

```python
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='docr_pkg',
     version='0.1',
     scripts=['docr'] ,
     author="Shakil Hossain",
     author_email="shakil.shaion@gmail.com",
     description="A pip package for test purpose",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/shaionbd/docr_pkg",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
``` 

#### Compiling projects

```
$ python setup.py bdist_wheel
```
* <b>build:</b> build package information.

* <b>dist:</b> Contains your .whl file. A WHL file is a package saved in the Wheel format, which is the standard built-package format used for Python distributions. You can directly install a .whl file using pip install some_package.whl on your system

* <b>project.egg.info:</b> An egg package contains compiled bytecode, package information, dependency links, and captures the info used by the setup.py test command when running tests.

#### Create .pypirc file which stores the PyPi repo and paste this code on .pypirc file
```
$ touch .pypirc

[distutils]
index-servers=pypi
[pypi] 
repository = https://upload.pypi.org/legacy/ 
username = shaionbd
```
*** Here add your username of PyPi

<b>\[Note\]:</b> Create an account at PyPi [https://pypi.org/account/register/]

#### Upload your pip project at <b>PyPi</b>

```
$ python -m twine upload dist/*
```