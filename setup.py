# read the contents of your README file
from os import path

from setuptools import setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
	long_description = f.read()

setup(name='cbpi4-PIDArduino',
      version='0.0.6',
      description='CraftBeerPi4 PID Kettle Control Plugin',
      author='David Kelly',
      author_email='bluemodena@gmail.com',
      url='https://github.com/bluemodena/cbpi4-PIDArduino',
      license='GPLv3',
      include_package_data=True,
      package_data={
	      # If any package contains *.txt or *.rst files, include them:
	      '': ['*.txt', '*.rst', '*.yaml'],
	      'cbpi4-PIDArduino': ['*', '*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-PIDArduino'],
      install_requires=[
	      'cbpi>=4.0.0.52',
      ],
      long_description=long_description,
      long_description_content_type='text/markdown'
      )
