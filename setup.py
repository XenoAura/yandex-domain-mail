from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='yandex-domain-mail',
    version='0.1',
    description='Yandex domain mail API wrapper',
    url='https://github.com/XenoAura/yandex-domain-mail',
    author='Nikolay Mityukov',
    author_email='xenoaura@gmail.com',
    license='GNU GENERAL PUBLIC LICENSE',
    packages=['yandex-domain-mail'],
    install_requires=[
        'requests',
    ],
    long_description=open(join(dirname(__file__), 'README.md')).read(),
)
