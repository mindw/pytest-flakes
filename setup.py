from setuptools import setup

setup(
    name='pytest-flakes',
    description='pytest plugin to check source code with pyflakes',
    long_description=open("README.rst").read(),
    license="MIT license",
    use_scm_version={
        'version_scheme': 'guess-next-dev',
        'local_scheme': 'dirty-tag',
    },
    setup_requires=[
        'setuptools>=18.0',
        'setuptools-scm>1.5.4'
    ],
    author='Florian Schulze, Holger Krekel and Ronny Pfannschmidt',
    author_email='florian.schulze@gmx.net',
    url='https://github.com/fschulze/pytest-flakes',
    py_modules=['pytest_flakes'],
    entry_points={'pytest11': ['flakes = pytest_flakes']},
    install_requires=['pytest>=2.8', 'pyflakes']
)
