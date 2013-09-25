#!/usr/bin/env python3
###############################################################################
# Copyright © 2013, SVAKSHA (https://github.com/svaksha) AllRightsReserved.
# License: AGPLv3 License <http://www.gnu.org/licenses/agpl.html>
# All copies must retain this permission notice with the copyright notice.
###############################################################################

from distutils.core import setup
#from setuptools import setup, find_packages
import os, sys
import shutil
import warnings
import COD

def read():
    with open('README.rst') as f:
        return f.readfile()

PKGNAME='COD',
#VERSION=COD.__version__,
AUTHOR="SVAKSHA",
AUTHOR_EMAIL="svaksha@gmail.com",
LICENSE='AGPLv3',
URL='https://github.com/svaksha/COD',
DESCRIPTION=('Crystal structures'),
LONG_DESCRIPTION=open('README.rst').read()
PACKAGES=['COD'
          'COD.crystals',
          'COD.tests',
          ],   #TODO, tests
PACKAGE_DATA={'COD':['LICENSE.rst',
                     'AUTHORS.rst',
                     'README.rst',
                     ],
              'COD.crystals': ['/*.py'],
              'COD.tests': ['/*.py']
              },
CLASSIFIERS=['Development Status :: 13.08 - Alpha',
             'Intended Audience :: Developers',
             'License :: OSI Approved :: AGPLv3 License',
             'Programming Language :: Python :: 3.3',
             'Topic :: Scientific :: Chemistry',
             ],


setup(name=PKGNAME,
#     version=VERSION,
      maintainer=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      url=URL,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      packages=PACKAGES,
      package_data=PACKAGE_DATA,
      include_package_data = True,
      install_requires = ['Cython==0.19.1',
                          'Pillow==2.1.0',
                          'numpy==1.7.1',
                          'matplotlib==1.3.0',
                          'nose==1.3.0',
                          'pandas==0.12.0',
                          'patsy==0.2.1',
                          'pyparsing==2.0.1',
                          'python-dateutil==2.1',
                          'pytz==2013b',
                          'scipy==0.12.0',
                          'tornado==3.1',
                          ],
      classifiers=CLASSIFIERS,
      )

