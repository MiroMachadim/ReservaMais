class Pessoa:
    def __init__(self, nome: str, email: str, telefone1: str, telefone2):
        self.__nome = nome
        self.__email = email
        self.__telefone1 = telefone1
        self.__telefone2 = telefone2
        # em casos onde não se possui telefone2 no construtor será usado None
