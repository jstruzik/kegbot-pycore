#!/usr/bin/env python
"""Standalone Python Kegbot Core.

For more information, see http://kegbot.org/docs/pycore/
"""
from setuptools import setup, find_packages

DOCLINES = __doc__.split('\n')

VERSION = '1.0.3-pre'
SHORT_DESCRIPTION = DOCLINES[0]
LONG_DESCRIPTION = '\n'.join(DOCLINES[2:])

def setup_package():
  setup(
      name = 'kegbot-pycore',
      version = VERSION,
      description = SHORT_DESCRIPTION,
      long_description = LONG_DESCRIPTION,
      author = 'mike wakerly',
      author_email = 'opensource@hoho.com',
      url = 'http://kegbot.org/docs/pycore',
      packages = find_packages(exclude=['testdata']),
      namespace_packages = ['kegbot'],
      scripts = [
        'bin/kegboard_daemon.py',
        'bin/kegbot_core.py',
        'bin/lcd_daemon.py',
        'bin/rfid_daemon.py',
        'bin/test_flow.py',
      ],
      install_requires = [
        'distribute',
        'kegbot-pyutils >= 0.1.4',
        'kegbot-api >= 0.1.2',
        'kegbot-kegboard >= 1.0.0',

        'python-gflags >= 1.8',
      ],
      include_package_data = True,
  )

if __name__ == '__main__':
  setup_package()
