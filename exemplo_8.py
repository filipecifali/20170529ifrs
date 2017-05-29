def imports():
    """
    >>> print('E falando de classes, voce pode transformar elas em modulos')
    'E falando de classes, voce pode transformar elas em modulos'
    >>> from doto import Doto # arquivo da classe doto.py
    >>> from random import choice # adiciona ao namespace atual somente a funcao choice
    >>> from random import * # adiciona todas as funcoes e sao chamadas pelos nomes
    >>> import random # adiciona tudo mas precisa chamar por random.choice (i.e)
    """

if __name__ == "__main__":
    import doctest
    docttest.testmod()
