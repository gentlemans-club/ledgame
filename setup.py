from distutils.core import setup

setup(
    name='ledgame',
    version='0.0.1',
    author='gentlemans-club',
    author_email='kentsd16@student.uia.no',
    packages=['ledgame'],
    python_requires='>=3.6.0',
    install_requires=[
        'notpi'
    ],
    dependency_links=['git+https://github.com/gentlemans-club/notpi.git@master#egg=notpi-0']
)
