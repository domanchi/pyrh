from setuptools import find_packages
from setuptools import setup


setup(
    name='pyrh',
    packages=find_packages(exclude=(['test*', 'tmp*'])),
    version='2.0',
    license='MIT',
    install_requires=[
        'marshmallow',
        'python-dateutil',
        'pytz',
        'requests',
        'yarl',
        'certifi',
    ],
)
