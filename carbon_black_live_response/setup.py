# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name='carbon_black_live_response-rapid7-plugin',
      version='1.0.0',
      description='The Cb Response Live Response feature allows security operators to collect information and take action on remote endpoints in real time. These actions include the ability to upload, download, and remove files, retrieve and remove registry entries, dump contents of physical memory, execute and terminate processes',
      author='rapid7',
      author_email='',
      url='',
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_carbon_black_live_response']
      )
