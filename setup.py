from setuptools import setup

with open("Readme.rst", 'r') as f:
    long_description = f.read()

setup(
   name='foo',
   version='1.0',
   description='A useful module',
   license="GNU GPLv2",
   long_description=long_description,
   author='Michal Gabaja,
   author_email='michal.gabaja@hotmail.com',
   url="http://www.foopackage.com/",
   packages=['vodafone'],  #same as name
   
  
