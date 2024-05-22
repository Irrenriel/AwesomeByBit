import setuptools

setuptools.setup(
    include_package_data=True,
    name='awesomebybit',
    version='0.0.1',
    description='Awesome async lib for working with ByBit!',
    url='https://github.com/Irrenriel/AwesomeByBit',
    author='Irrenriel',
    packages=setuptools.find_packages(),
    install_requires=[
        'aiohttp>=3.9.3', 'pydantic>=2.5.3'
    ],
    long_description='Awesome async lib for working with ByBit!',
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
    ],
)