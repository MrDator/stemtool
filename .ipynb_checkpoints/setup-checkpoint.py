from setuptools import setup, find_packages

exec(open('stemtools/version.py').read())

setup(name='stemtools',
    version=__version__,
    packages=find_packages(),
    description='Analysis of aberration corrected STEM data and 4D STEM data',
    url='https://code.ornl.gov/7dm/stemtools',
    author='Debangshu Mukherjee',
    author_email='mukherjeed@ornl.gov',
    license='GNU GPLv3',
    keywords="STEM",
    install_requires=[
        'numpy >= 1.15, < 2.0',
        'scipy >= 1.1, < 1.2',
    ])