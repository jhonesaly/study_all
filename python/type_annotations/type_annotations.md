# Type Annotations

 Type annotations são uma forma de especificar os tipos de dados esperados em uma determinada variável, argumento de função ou valor de retorno de função. As type annotations podem ajudar a tornar o código mais legível, mais fácil de entender e mais fácil de manter.

## Python

Em python, para tal, se utiliza a biblioteca "mypy". PAra instálá-la, use:

    pip install mypy
    pip install flake8

Em settings.json, antes da última chaves, adicione as seguintes configurações:

    "python.linting.flake8Enabled": true,
    "python.linting.mypyEnabled": true,

Isso permitirá que você faça algumas tarefas sem ter de executar o mypy diretamente no terminal.
