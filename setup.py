# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '2.0'

setup(name='paraiba.portal',
      version=version,
      description="Pacote de política do portal do Governo do Estado da Paraíba.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Alyson de Castro',
      author_email='alysoncastro@codata.pb.gov.br',
      url='https://github.com/alysondecastro/paraiba.portal.git',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['paraiba'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.nitf',
          'collective.cover',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': ['plone.app.testing',]
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
