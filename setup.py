#!/usr/bin/env python
import os

from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def find_package_data(pkg, filetypes):
    import glob
    import itertools

    out = []
    for f in filetypes:
        for x in range(0, 20):
            pattern = pkg + '/' + ('*/' * x) + f
            out.extend([p[len(pkg)+1:] for p in glob.glob(pattern)])
    return out

setup(
    name = 'django-wiki',
    version = '0.4',
    url = 'http://github.com/spookylukey/django-wiki',
    license = 'BSD License',
    description = 'A Django wiki application.',
    long_description = read('README.rst'),
    packages = find_packages(),
    package_data = {
        'djiki': find_package_data('djiki', ['*.png', '*.html', '*.css', '*.js'])
        },

    install_requires = [
        'setuptools',
        'creole',
        ],

    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        ],
)
