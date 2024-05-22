from setuptools import setup, find_packages

setup(
    name='AwesomeByBit',
    version='0.1.0',
    install_requirements=[
        'aiohttp == 3.9.3',
        'pydantic == 2.5.3'
    ],
    packages=find_packages(
        where='AwesomeByBit'
    )
)