class Fantasmas:
    def __init__(self, fantasma, linhaInicial, colunaInicial):
        self.fantasma = fantasma
        self.linha = linhaInicial
        self.coluna = colunaInicial
        
    def moverEsquerda(self, mapa):
        if mapa[self.linha][self.coluna - 1] not in ['\033[34;1m#\033[m', "\033[0;31mR\033[m", "\033[32mG\033[m", "\033[94mB\033[m", "\033[33mY\033[m"]:
            self.coluna -= 1

    def moverDireita(self, mapa):
        if mapa[self.linha][self.coluna + 1] not in ['\033[34;1m#\033[m', "\033[0;31mR\033[m", "\033[32mG\033[m", "\033[94mB\033[m", "\033[33mY\033[m"]:
            self.coluna += 1

    def moverCima(self, mapa):
        if mapa[self.linha - 1][self.coluna] not in ['\033[34;1m#\033[m', "\033[0;31mR\033[m", "\033[32mG\033[m", "\033[94mB\033[m", "\033[33mY\033[m"]:
            self.linha -= 1

    def moverBaixo(self, mapa):
        if mapa[self.linha + 1][self.coluna] not in ['\033[34;1m#\033[m', "\033[0;31mR\033[m", "\033[32mG\033[m", "\033[94mB\033[m", "\033[33mY\033[m"]:
            self.linha += 1
