def pegue_me_se_puder():
    """
    >>> print('E chegamos a topicos mais serios... ')
    >>> def divisao_que_nao_criaram_teste(x, y):
    >>>     try:
    >>>         x/y
    >>>     except:
    >>>         print('Voce nao vai mesmo testar o y?')
    >>>     finally:
    >>>         return 42
    >>> divisao_que_nao_criaram_teste(1, 0)
    'Voce nao vai mesmo testar o y?'
    42
    >>> print('Existem diversos tipos de exception e voce pode criar as suas')
    'Existem diversos tipos de exception e voce pode criar as suas'
    """

if __name__ == "__main__":
    import doctest
    docttest.testmod()
