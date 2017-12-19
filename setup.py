from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

install_requires = [
    # List your project dependencies here.
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]


setup(name='markov',
    version=version,
    description="Markov Chain generator from random process data",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
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
    url='https://github.com/vladignatyev/markov',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    entry_points={
        'console_scripts':
            ['markov=markov:main']
    }
)
