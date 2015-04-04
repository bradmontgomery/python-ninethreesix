from setuptools import setup
from ninethreesix import __version__

setup(
    name='python-ninethreesix',
    version=__version__,
    description="a password generator inspired by http://xkcd.com/936/",
    long_description=open('README.rst').read(),
    author='Brad Montgomery',
    author_email='brad@bradmontgomery.net',
    url='https://github.com/bradmontgomery/python-ninethreesix',
    license='MIT',
    packages=['ninethreesix'],
    include_package_data=True,
    package_data={'': ['README.rst']},
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
