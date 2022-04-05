from setuptools import setup

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyostal',
    version='0.8.1',
    description='A Python lightweight Postal API Client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords='postal postalserver email http client events',
    url='http://github.com/rnevarezc/pyostal',
    author='Rafael Nevarez',
    license='MIT',
    packages=['pyostal'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'requests', 'pydantic'
    ],
    zip_safe=False
)