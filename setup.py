from setuptools import setup, find_packages

setup(
    name='betdaqlightweight',
    version='0.0.2b',
    packages=find_packages(),
    url='https://github.com/bbezias/betdaqlightweight',
    license='GNU',
    author='Benjamin Bezias',
    author_email='benjaminbezias@gmail.com',
    install_requires=[line.strip() for line in open("requirements.txt")],
    description=''
)
