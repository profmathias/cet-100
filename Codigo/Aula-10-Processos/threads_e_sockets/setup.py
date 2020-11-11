from setuptools import setup

setup(
    name='threads_and_sockets',
    version="0.0.1",
    author="Mathias Santos de Brito",
    author_email="msbrito@uesc.br",
    description=("Utilização do módulo socket para atender requisições"
                 " simples vindas de clientes."),
    license="GNU",
    keywords="exercicio sd uesc",
    url="http://github.com/profmathias/cet-100",
    packages=['app'],
    install_requires='',
    entry_points={
        'console_scripts': [
            'thread-and-sockets-server=app.aula8_fixed_server:main',
            'thread-and-sockets-client=app.aula8_fixed_client:main'
        ]
    }
)
