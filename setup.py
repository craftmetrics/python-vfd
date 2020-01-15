from setuptools import setup


setup(
    # Package Metadata
    name='python-vfd',
    version=0.1,
    author='Luke Cyca',
    author_email='luke@craftmetrics.ca',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
    ],
    packages=['vfd'],
    install_requires=[
        'umodbus'
    ],
)
