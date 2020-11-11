from setuptools import setup

setup(
    name='sd_descoberta',
    version="0.0.0",
    author="Mathias Santos de Brito",
    author_email="msbrito@uesc.br",
    description=("mDNS/DNS-SD com Python Zeroconf"),
    license="GNU",
    keywords="exemplo zeroconf DNS-SD mDNS UESC",
    url="http://github.com/profmathias/cet-100",
    packages=['app_descoberta'],
    long_description='Este é um exemplo de aplicação que escuta a rede para encontrar '
                     'serviços utlizando DNS-SD/mDNS.',
    install_requires='zeroconf',
    entry_points={
        'console_scripts': [
            'sd_descoberta=app_descoberta.main:main'
        ]
    }
)
