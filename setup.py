from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1a'

install_requires = []


setup(name='markovfsm',
    version=version,
    description="Markov Chain generator from random process data",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.6',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.2',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Python :: 3.4',
      'Topic :: Software Development :: Libraries',
      'Topic :: Scientific/Engineering :: Information Analysis',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
      'License :: OSI Approved :: MIT License',
      'Natural Language :: English'
    ],
    keywords='markov chain random process probability stochastic automata finite-state machine fsm',
    author='Vladimir Ignatev',
    author_email='ya.na.pochte@gmail.com',
    url='https://github.com/vladignatyev/markovfsm',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires
)
