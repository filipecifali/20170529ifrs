def funcoes():
    """
    >>> # Para criar funcoes / metodos em Python, usa-se a keyword 'def'
    >>> def exemplo_de_funcao(x, y):
    >>>     return x + y
    >>>
    >>> exemplo_de_funcao(1, 2)
    3
    >>> def argumentos_dinamicos(*args):
    >>>     print('args')
    >>>     for arg in args:
    >>>         print(arg)
    >>>
    >>> def argumentos_dinamicos_kv(**kwargs):
    >>>     print('kwargs')
    >>>     for key, value in kwargs.items():
    >>>         print(key, value)
    >>>
    >>> argumentos_dinamicos('a', 'b', 'c')
    'args'
    'a'
    'b'
    'c'
    >>> argumentos_dinamicos_kv(nome='Filipe', sobrenome='Cifali', hobby='NYXNYXNYX')
    'kwargs'
    'nome Filipe'
    'sobrenome Cifali'
    'hobby NYXNYXNYX'
    """

if __name__ == "__main__":
    import doctest
    docttest.testmod()
