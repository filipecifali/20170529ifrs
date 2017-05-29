def classes():
    """
    >>> print('Ta mas... cade a orientacaoo a blobjetos?')
    'Ta mas... cade a orientacao a blobjetos?'
    >>> class Doto:
    >>>     atrib = 'Truth compels me.'
    >>>
    >>>     def __init__(self):
    >>>         self.do_some_black_majecs()
    >>>
    >>>     def do_some_bkack_majecs(self):
    >>>         print('Magic is an abomination. Magic thyself out of that.')
    >>>         print(atrib)
    >>>
    >>> b = Doto
    'Magic is an abomination. Magic thyself out of that.'
    'Truth compels me.'
    >>> print('A palavra "self" e usada para mapear a instancia do objeto')
    'A palavra "self" e usada para mapear a instancia do objeto'
    """

if __name__ == "__main__":
    import doctest
    docttest.testmod()
