from setuptools import setup

setup(
    name='grpc_client',
    version='0.0.0',
    author='Mathias Santos de Brito',
    author_email='msbrito@uesc.br',
    description=('Um cliente simples para um servidor simples usando gRPC.'),
    license='GNU',
    keywords='grpc "sistemas distribuídos" uesc',
    url='http://github.com/profmathias/cet-100',
    packages=['grpc_client'],
    long_description='Este projeto faz parte da disciplina de Sistemas Distribuídos'
                     'da UESC e visa introduzir na prática os conceitos de RPC com o '
                     'gRPC.',
    install_requires='',
    entry_points={
        'console_scripts': [
            'grpc_client=grpc_client.main:main'
        ]
    }
)
