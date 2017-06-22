from setuptools import setup

setup(
    name = 'ramka',
    version = 170620,
    license = 'MIT',
    py_modules = ['ramka'],
    install_requires = [ 'pyperclip' ],
    entry_points = {
        'console_scripts': [
            'ramka = ramka:main',
            'ramka-fort = ramka:fortran_procedure',
        ],
    },
)
