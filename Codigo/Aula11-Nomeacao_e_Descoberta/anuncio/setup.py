from setuptools import setup

setup(
    name='sd_anuncio',
    version="0.0.0",
    author="Mathias Santos de Brito",
    author_email="msbrito@uesc.br",
    description=("Anuncion de serviço cp, mDNS/DNS-SD e Python Zeroconf"),
    license="GNU",
    keywords="exemplo zeroconf DNS-SD mDNS UESC",
    url="http://github.com/profmathias/cet-100",
    packages=['app_anuncio'],
    long_description='Este é um exemplo de aplicação que anuncia um'
                     'serviço utlizando DNS-SD/mDNS.',
    install_requires='zeroconf',
    entry_points={
        'console_scripts': [
            'sd_anuncio=app_anuncio.main:main'
        ]
    }
)
