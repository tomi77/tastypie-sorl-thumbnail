from codecs import open

from setuptools import setup, find_packages

setup(
    name="django-tastypie-sorl-thumbnail",
    version='0.1.5',
    author='Tomasz Jakub Rup',
    author_email='tomasz.rup@gmail.com',
    url='https://github.com/tomi77/tastypie-sorl-thumbnail',
    description='sorl-thumbnail support for a Django Tastypie',
    long_description=open("README.rst").read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    license='MIT',
    packages=find_packages(exclude=['testapp']),
    install_requires=[
        'django-tastypie',
        'sorl-thumbnail',
    ],
    test_suite='testapp.runtests.runtests',
    tests_require=[
        'six',
        'django',
        'mock',
        'pyyaml',
        'pillow',
    ]
)
