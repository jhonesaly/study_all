from setuptools import setup, find_packages

setup(
    name='algoritmos',
    version='0.23.2.13',
    author='Alyson Jhones',
    author_email='jhonesaly@gmail.com',
    description='Pacote contendo todos os algoritmos desenvolvidos até o momento da versão (0.ano.mês.dia)',
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib'],
)