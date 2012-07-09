#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='django-oscar-jirafe',
      version='0.1',
      url='https://github.com/tangentlabs/django-oscar-jirafe',
      author="David Winterbottom",
      author_email="david.winterbottom@tangentlabs.co.uk",
      description="Jirafe module for django-oscar",
      long_description=open('README.rst').read(),
      keywords="Payment, Jirafe",
      license='BSD',
      packages=find_packages(),
      include_package_data = True,
      # See http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: Unix',
                   'Programming Language :: Python'],
      install_requires=['django-oscar>=0.2']
     )
