from setuptools import setup

setup(
    name='billomapy',
    version='2.6',
    install_requires=['requests>=2.20.0'],
    packages=['billomapy'],
    url='https://github.com/seibert-media/billomapy',
    license='Apache License 2.0',
    author='Michael Bykovski, Jean Petry',
    author_email='jpetry@seibert-media.net',
    description='A Python library for http://www.billomat.com/'
)
