class Andar:
    qtQuartos = 6
    id = 0

    def __init__(self):
        self.quartosDisponiveis = list(
            range(Andar.id * Andar.qtQuartos, Andar.qtQuartos * (Andar.id + 1))
        )  # A criação dos quartos é automatica usando id e qtQuartos
        Andar.id += 1
        self.quartosOcupados = (
            list()
        )  # lista vazia criada no começo já que tem 0 quartos ocupados ao criar o andar
