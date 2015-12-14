from setuptools import setup

setup(
    name="gravtr",
    version="0.0.1",

    description="Simple gravatar url generator",

    # The project URL.
    url='https://github.com/gfabricio/gravtr',

    # Author details
    author='Guilherme Fabricio',
    author_email='gfabricio@gmail.com',

    # Choose your license
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        # Who the project is intended for.
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',

        # Supported Python versions.
        'Programming Language :: Python :: 2.7, 3.4',
    ],
    keywords='gravatar avatar gravtr',
    packages=['gravtr'],
)
