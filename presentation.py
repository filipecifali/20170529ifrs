"""
>>> print("Bem-vindos a Introdução a Python 3 [!!]")
"Bem-vindos a Introdução a Python 3"
"""

def exemplo_0_porque_usar():
    """
    >>> print('Quem sou eu?')
    'Quem sou eu?'
    >>> print('Filipe Cifali')
    'Filipe Cifali'
    >>> print('Trabalho como sysadmin na KingHost no núcleo de Linux desde 2010')
    'Trabalho como sysadmin na KingHost no núcleo de Linux desde 2010'
    >>> print('Porque usar python?')
    'Porque usar python?'
    >>> import antigravity
    >>> import this
    'The Zen of Python, by Tim Peters \

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!'
    >>> print('Linguagem dinamica e fortemente tipada')
    'Linguagem dinamica e fortemente tipada'
    >>> print('Criada para ser uma linguagem de facil uso')
    'Criada para ser uma linguagem de facil uso'
    >>> print('Mas quem usa essa coisa? É uma cobra afinal de contas...')
    'Mas quem usa essa coisa? É uma cobra afinal de contas...'
    >>> print(lista_empresas[:6])
    ['Globocom', 'Google', 'Magazine Luiza', 'SERPRO', 'ZNC Sistemas', 'TOTVS']
    >>> print('Uma das comunidades mais ativas do Brasil')
    'Uma das comunidades mais ativas do Brasil'
    >>> print('Acesse http://python.org.br/ e descubra mais :)')
    'Acesse http://python.org.br/ e descubra mais :)'
    """

def exemplo_1_strings():
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

    >>> print('Ele também consegue fazer slicing de maneira bem prática')
    'Ele também consegue fazer slicing de maneira bem prática'
    >>> print(nome[0])
    'F'
    >>> print(nome[-1])
    'e'
    >>> print(nome[1:])
    'ilipe'
    >>> print(nome[:1])
    'F'
    >>> print('E consegue até mesmo inverter strings usando o slicing')
    'E consegue até mesmo inverter strings usando o slicing'
    >>> print(nome[::-1])
    'epiliF'
    """

def exemplo_2_ints():
    """
    >>> # Basicamente Python também sabe um pouquinho de matemática
    >>> print(10 + 2)
    '12'
    >>> print(2 * 6)
    '12'
    >>> print(36 / 3)
    '12.0'
    """

def exemplo_3_funcoes():
    """
    >>> # Para criar funções / métodos em Python, usa-se a keyword 'def'
    >>> def exemplo_de_funcao(x, y):
    >>>     return x + y
    >>> exemplo_de_funcao(1, 2)
    3
    """

def exemplo_4_lacos_e_condicionais():
    """
    >>> print('Os laços condicionais são bem simples de se usar')
    'Os laços condicionais são bem simples de se usar'
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
    """

def exemplo_5_pegue_me_se_puder():
    """
    >>> print('E chegamos a tópicos mais sérios... ')
    >>> def divisao_que_nao_criaram_teste(x, y):
    >>>     try:
    >>>         x/y
    >>>     except:
    >>>         print('Você não vai mesmo testar o y?')
    >>>     finally:
    >>>         return 42
    'Você não vai mesmo testar o y?'
    42
    >>> print('Existem diversos tipos de exceção e você pode criar as suas')
    'Existem diversos tipos de exceção e você pode criar as suas'
    """

def exemplo_6_classes():
    """
    >>> print('Tá mas... cadê a orientação a blobjetos?')
    'Tá mas... cadê a orientação a blobjetos?'
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
    >>> print('A palavra "self" é usada para mapear a instancia do objeto')
    'A palavra "self" é usada para mapear a instancia do objeto'
    """

def exemplo_7_imports():
    """
    >>> print('E falando de classes, você pode transformar elas em módulos')
    'E falando de classes, você pode transformar elas em módulos'
    >>> from doto import Doto # arquivo da classe doto.py
    >>> from random import choice # adiciona ao namespace atual somente a função choice
    >>> from random import * # adiciona todas as funções e são chamadas pelos nomes
    >>> import random # adiciona tudo mas precisa chamar por random.choice (i.e)
    """

def exemplo_8_toolkit():
    """
    >>> print('O pip é o instalador de pacotes mais recomendado atualmente')
    'O pip é o instalador de pacotes mais recomendado atualmente'
    >>> print('Para desenvolvimento web os frameworks mais populares são:')
    'Para desenvolvimento web os frameworks mais populares são:'
    >>> for top in top_web_frameworks:
    >>>     print(top)
    'Django'
    'Flask'
    'Tornado'
    'Web2py'
    'Pyramid'
    >>> print('')
    """

def exemplo_final():
    """
    >>> for quote in best_quotes:
    >>>     print(quote)
    'King Arthur: I am your king.'
    'Woman: Well, I didn't vote for you.'
    'King Arthur: You don't vote for kings.'
    'Woman: Well, how'd you become a king then?'
    'King Arthur: The Lady of the Lake, her arm clad in the purest shimmering samite \
        held aloft Excalibur from the bosom of the water, signifying by divine
        providence that I, Arthur, was to carry Excalibur. THAT is why I am your king.'
    'Dennis: Listen, strange women lyin' in ponds distributin' swords is no basis for \
            a system of government. Supreme executive power derives from a mandate
            from the masses, not from some farcical aquatic ceremony.'
    """

if __name__ == "__main__":
    import doctest
    docttest.testmod()
