from setuptools import setup, find_packages

setup(name='jostman',
      version='1.0',
      description="Jun's own api checker",
      author='Jun',
      author_email='jun@junaire.com',
      packages=find_packages(),
      install_requires=['requests'],
      entry_points = {
        'console_scripts': ['jostman=src.jostman:main'],
        },
      zip_safe=False)

