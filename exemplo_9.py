def toolkit():
    """
    >>> print('O pip e o instalador de pacotes mais recomendado atualmente')
    'O pip e o instalador de pacotes mais recomendado atualmente'
    >>> print('Para desenvolvimento web os frameworks mais populares sao:')
    'Para desenvolvimento web os frameworks mais populares sao:'
    >>> for top in top_web_frameworks:
    >>>     print(top)
    'Django'
    'Flask'
    'Tornado'
    'Web2py'
    'Pyramid'
    """

if __name__ == "__main__":
    import doctest
    docttest.testmod()
