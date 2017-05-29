def tipos_de_dados:
    """
    >>> lista = [1, 2, 3] # Mutantes, mutaveis e flexiveis, nao muito rapidas
    >>> print(lista[1])
    2
    >>> lista.append(4)
    >>> print(lista)
    [1, 2, 3, 4]
    >>> tupla = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun',
            'jul', 'ago', 'set', 'out', 'nov', 'dez') # Tuplas sao imutaveis,
    >>> # uteis para dados estaticos mas nem sempre mais rapidas
    >>> dicts = {hero='Nyx', role='Gankerino', kda='4.2'}
    >>> # Dicionarios sao interessantes pois podem receber dados de maneira serializada
    """

if __name__ == "__main__":
    import doctest
    docttest.testmod()
