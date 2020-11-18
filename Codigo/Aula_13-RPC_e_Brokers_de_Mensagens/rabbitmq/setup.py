from setuptools import setup

setup(
    name='rabbitmq_ex',
    version="0.0.1",
    author="Mathias Santos de Brito",
    author_email="msbrito@uesc.br",
    description=("Exemplo de comunicação utilizando RabbitMQ"),
    license="GNU",
    keywords="'Sistemas Distribuídos' rabbitmq uesc",
    url="http://github.com/profmathias/cet-100",
    packages=['rabbitmq_ex'],
    long_description='Esse é um exemplo de comunicação entre um servidor que utiliza'
                     'RabbitMQ para servir os seus cliente. Este exemplo é para da '
                     'disciplina de Sistemas Distribuídos da UESC',
    install_requires='pika',
    entry_points={
        'console_scripts': [
            'rabbitmq_ex=rabbitmq_ex.server:main'
        ]
    }
)
