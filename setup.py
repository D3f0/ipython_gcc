# encoding: utf-8
from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.0.1'

install_requires = [
    # 'prettytable',
    'ipython>=1.0',
    'six',
]


packages=find_packages('src')


setup(name='ipython-gcc',
    version=version,
    description="A nicer inetraction with plain old C from Python",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Topic :: Database',
        'Topic :: Database :: Front-Ends',
        # 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
    ],
    keywords='compiler ipython gcc',
    author='Nahuel Defossé',
    author_email='nahuel.defosse@gmail.com',
    url='pypi.python.org/pypi/ipython-gcc',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
)
