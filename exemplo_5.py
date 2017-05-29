def lacos_e_condicionais():
    """
    >>> print('Os lacos condicionais sao bem simples de se usar')
    'Os lacos condicionais sao bem simples de se usar'
    >>> from random import randint
    >>> num_sorteado = randint(0, 9)
    >>> print(num_sorteado)
    5
    >>> if num_sorteado > 5:
    >>>     print('>')
    >>> elif num_sorteado < 5:
    >>>     print('<')
    >>> elif num_sorteado == 5:
    >>>     print('==')
    >>> else:
    >>>     print('>=<')
    '=='
    >>> exemplos_usados = ['letras', 'numeros', 'funcoes', 'loops']
    >>> for e in exemplos_usados:
    >>>     print(e)
    'letras'
    'numeros'
    'funcoes'
    'loops'
    >>> while True:
    >>>     print('Do you want ants? That\'s how you get ants!!')
    >>>     break
    'Do you want ants? That's how you get ants!!'
    >>> if 1 == True:
    >>>     print('V')
    >>> else:
    >>>     print('F')
    'V'
    >>> if 1 is True:
    >>>     print('F')
    >>>
    >>> print('Isso ocorre porque o operador "is" testa o objeto tambem')
    'Isso ocorre porque o operador "is" testa o objeto tambem'
    """

if __name__ == "__main__":
    import doctest
    docttest.testmod()
