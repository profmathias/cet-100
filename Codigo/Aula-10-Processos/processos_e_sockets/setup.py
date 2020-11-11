from setuptools import setup

setup(
    name='threads_and_processes',
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
            'thread-and-processes-server=app.sockets_e_processos_server:main',
            'thread-and-processes-client=app.sockets_e_processos_client:main'
        ]
    }
)
