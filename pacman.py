class Pacman:
    def __init__(self, pacman, linhaInicial, colunaInicial):
        self.pacman = pacman
        self.linha = linhaInicial
        self.coluna = colunaInicial

    def moverEsquerda(self):
        self.coluna -= 1

    def moverDireita(self):
        self.coluna += 1

    def moverCima(self):
        self.linha -= 1

    def moverBaixo(self):
        self.linha += 1