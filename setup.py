import os
import sys
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
    
requirements = ['httplib2', 'argparse']
try:
    import json
except ImportError:
    requirements.append('simplejson')

setup(
    name = "python-hdcloud",
    version = "1.0",
    description = "Client library for the HD Cloud API",
    long_description = read('README.rst'),
    url = 'http://packages.python.org/python-hdcloud',
    license = 'BSD',
    author = 'Jacob Kaplan-Moss',
    author_email = 'jacob@jacobian.org',
    packages = find_packages(exclude=['tests']),
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = requirements,
    tests_require = ["nose", "mock"],
    test_suite = "nose.collector",
)