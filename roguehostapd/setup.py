"""
Module for setup hostapd shared library
"""

import os
import shutil
try:
    from setuptools import setup
    from setuptools.command.install import install
except ImportError:
    from distutils.core import setup
    from distutils.command.install import install
from distutils.command.build_ext import build_ext
import roguehostapd.buildutil.buildcommon as buildcommon
import roguehostapd.buildutil.buildexception as buildexception
from roguehostapd.config.hostapdconfig import WHITE, RED

# Create tmp directory if it doesn't exist
if not os.path.exists('tmp'):
    os.makedirs('tmp')

# define project information
NAME = 'roguehostapd'
PACKAGES = [
    'roguehostapd', 
    'examples', 
    'roguehostapd.config', 
    'roguehostapd.buildutil'
]
PACKAGE_DIR = {'roguehostapd': 'roguehostapd'}
PACKAGE_DATA = {'roguehostapd': ['config/hostapd.conf', 'config/config.ini']}
VERSION = '1.1.2'
DESCRIPTION = 'Hostapd wrapper for hostapd'
URL = 'https://github.com/wifiphisher/roguehostapd'
AUTHOR = 'Anakin'

try:
    EXT_MODULE = buildcommon.get_extension_module()
    setup(
        name=NAME,
        packages=PACKAGES,
        package_dir=PACKAGE_DIR,
        package_data=PACKAGE_DATA,
        version=VERSION,
        description=DESCRIPTION,
        url=URL,
        author=AUTHOR,
        install_requires=[],
        zip_safe=False,
        cmdclass={
            'build_ext': build_ext,
            'install': install
        },
        ext_modules=EXT_MODULE)
except buildexception.SharedLibMissError as exobj:
    print("[" + RED + "!" + WHITE + "] " +
          ("The development package for " + exobj.libname +
           " is missing. Please download it and restart the compilation."
           "If you are on Debian-based system: \'apt-get install{}\'.".format(
               "".join(" " + package for package in exobj.packages))))
finally:
    # Clean up the tmp directory safely
    if os.path.exists('tmp'):
        shutil.rmtree('tmp')
