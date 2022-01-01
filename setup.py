import os
from glob import glob
from setuptools import setup

exec(open('ternviz/version.py').read())

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(name='ternviz',
      version=__version__,
      description='Render SMILES into 3D video',
      author='Andrew White',
      author_email='andrew.white@rochester.edu',
      url='https://github.com/whitead/ternviz',
      license='MIT',
      packages=['ternviz', 'ternviz.vmd'],
      install_requires=[
          'click',
          'rdkit-pypi',
          'tweepy',
          'python-dotenv',
          'importlib_resources'],
      zip_safe=True,
      entry_points='''
        [console_scripts]
        ternviz=ternviz.main:main
        ternviz-bot=ternviz.bot:bot
            ''',
      package_data={'ternviz': ['vmd/*.vmd']},
      long_description=long_description,
      long_description_content_type="text/markdown",
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Topic :: Scientific/Engineering :: Chemistry",
      ]
      )
