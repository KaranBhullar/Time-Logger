from setuptools import setup, find_packages

setup(
    name='pyexample',
    version='1.0',    
    description='TimeLogger is a simple stopwatch CLI tool.',
    url='https://github.com/KaranBhullar/Time-Logger',
    author='Karan Bhullar',
    author_email='karanbhullar42@gmail.com',
    packages=find_packages(exclude='docs'),
    install_requires=['argparse'],
    entry_points={
          'console_scripts': ['timeLogger=timeLogger.timeLogger:main'],
      },

)
