def strings():
    """
    >>> print('Strings!! Vamos falar sobre strings!')
    'Strings!! Vamos falar sobre strings!'

    >>> print('Python sabe brincar com strings de maneira bem natural')
    'Python sabe brincar com strings de maneira bem natural'

    >>> nome = 'Filipe'
    >>> sobrenome = 'Cifali'
    >>> nome_completo = ' '.join([nome, sobrenome]))
    >>> print(nome_completo)
    >>> print(nome_completo.split(' ')[0])
    'Filipe'
    >>> print(nome_completo.split(' ')[1])
    'Cifali'

    >>> print('Ele tambem consegue fazer slicing de maneira bem pratica')
    'Ele tambem consegue fazer slicing de maneira bem pratica'
    >>> print(nome[0])
    'F'
    >>> print(nome[-1])
    'e'
    >>> print(nome[1:])
    'ilipe'
    >>> print(nome[:1])
    'F'
    >>> print('E consegue ate mesmo inverter strings usando o slicing')
    'E consegue ate mesmo inverter strings usando o slicing'
    >>> print(nome[::-1])
    'epiliF'
    """
    
if __name__ == "__main__":
    import doctest
    docttest.testmod()
