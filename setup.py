from setuptools import setup, find_packages

setup(
    name='algorithms',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'wheel',
        'pygraphviz',
    ],
    py_modules=['rcviz'],
)
