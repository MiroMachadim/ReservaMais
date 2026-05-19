import Gerente


class Hotel:
    def __init__(self):
        self.__nome = "ReservaMais"
        self.__andares = 5
        self.__precoEstadia = 40
        self.__tempoEstadia = None
        self.__gerente = Gerente.Gerente()
        self.__qtFuncionario = 0
        self.__Funcionarios = list()
