from setuptools import setup, find_packages

setup(
    name="selectivesearch",
    version="0.3",
    url="https://github.com/AlpacaDB/selectivesearch",
    description="Selective Search implementation for Python",
    author="AlpacaDB, Inc.",
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='rcnn',
    packages=find_packages(),
    install_requires=['numpy', 'scikit-image'],
)
