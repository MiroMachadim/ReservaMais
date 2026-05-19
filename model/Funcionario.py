import Pessoa


class Funcionario(Pessoa.Pessoa):
    __id = 0

    def __init__(self, senha, tipo):
        self.__senha = senha
        self.__tipo = tipo
        self.__nivelPermissao = 0
        Funcionario.__id += 1
