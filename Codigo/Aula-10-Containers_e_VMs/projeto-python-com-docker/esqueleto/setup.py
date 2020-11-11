from setuptools import setup

setup(
    name='meu_app',
    version="0.0.0",
    author="Eu Mesmo da Silva",
    author_email="eumesmo@example",
    description=("Esqueleto para aplicações Python com um Dockerfile."),
    license="GNU",
    keywords="esqueleto skeleton",
    url="http://github.com/profmathias/cet-100",
    packages=['app'],
    long_description='Uma descrição mais longa do projeto.',
    install_requires='',
    entry_points={
        'console_scripts': [
            'meu_app=app.main:main'
        ]
    }
)
