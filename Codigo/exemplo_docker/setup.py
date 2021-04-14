from setuptools import setup

setup(
    name="exemplo_docker",
    version='0.0.1',
    author='Mathias',
    description='',
    license='GNU',
    install_requires='flask',
    entry_points={
        'console_scripts': [
            'ex_docker=main:main'
        ]
    }

)
