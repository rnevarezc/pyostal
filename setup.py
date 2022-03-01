from setuptools import setup

setup(
    name='pyostal',
    version='0.5',
    description='A Python lightweight Postal API Client',
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
        'requests',
    ],
    zip_safe=False
)