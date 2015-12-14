from setuptools import setup

setup(
    name="gravtr",
    version="0.0.3",

    description="Simple gravatar url generator",

    # The project URL.
    url='https://github.com/gfabricio/gravtr',

    # Author details
    author='Guilherme Fabricio',
    author_email='gfabricio@gmail.com',

    # Choose your license
    license='MIT',

    use_2to3=True,

    classifiers=[
        'Development Status :: 3 - Alpha',

        # Who the project is intended for.
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: Utilities',

        'License :: OSI Approved :: MIT License',

    ],
    keywords='gravatar avatar gravtr',
    packages=['gravtr'],
)
