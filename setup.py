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