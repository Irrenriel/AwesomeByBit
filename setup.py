from setuptools import setup, find_packages

setup(
    name='AwesomeByBit',
    version='0.1.0',
    description='Awesome async lib for working with ByBit!',
    author='Irrenriel',
    url='https://github.com/Irrenriel/AwesomeByBit',
    install_requires=[
        'aiohttp == 3.9.3',
        'pydantic == 2.5.3'
    ],
    packages=find_packages(
        include=['AwesomeByBit*']
    )
)
