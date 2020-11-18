from setuptools import setup

setup(
    name='grpc_client',
    version='0.0.1',
    author='Mathias Santos de Brito',
    author_email='msbrito@uesc.br',
    description=('Um servidor simples simples usando gRPC.'),
    license='GNU',
    keywords='grpc "sistemas distribuídos" uesc',
    url='http://github.com/profmathias/cet-100',
    packages=['grpc_server'],
    long_description='Este projeto faz parte da disciplina de Sistemas Distribuídos'
                     'da UESC e visa introduzir na prática os conceitos de RPC com o '
                     'gRPC. Está é uma implementação simples de um servidor gRPC.',
    install_requires='grpcio',
    entry_points={
        'console_scripts': [
            'grpc_server=grpc_server.main:main'
        ]
    }
)
