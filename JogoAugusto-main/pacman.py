class Pacman:
    def __init__(self, pacman, linhaInicial, colunaInicial):
        self.pacman = pacman
        self.linha = linhaInicial
        self.coluna = colunaInicial

    def moverEsquerda(self, mapa):
        if mapa[self.linha][self.coluna - 1] != '\033[34;1m#\033[m':
            self.coluna -= 1

    def moverDireita(self, mapa):
        if mapa[self.linha][self.coluna + 1] != '\033[34;1m#\033[m':
            self.coluna += 1

    def moverCima(self, mapa):
        if mapa[self.linha - 1][self.coluna] != '\033[34;1m#\033[m':
            self.linha -= 1

    def moverBaixo(self, mapa):
        if mapa[self.linha + 1][self.coluna] != '\033[34;1m#\033[m':
            self.linha += 1