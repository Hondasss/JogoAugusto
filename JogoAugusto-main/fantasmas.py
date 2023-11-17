class Fantasmas:
    def __init__(self, fantasma, linhaInicial, colunaInicial):
        self.fantasma = fantasma
        self.linha = linhaInicial
        self.coluna = colunaInicial
        
    def moverEsquerda(self, mapa):
        if mapa[self.linha][self.coluna - 1] != '#':
            self.coluna -= 1

    def moverDireita(self, mapa):
        if mapa[self.linha][self.coluna + 1] != '#':
            self.coluna += 1

    def moverCima(self, mapa):
        if mapa[self.linha - 1][self.coluna] != '#':
            self.linha -= 1

    def moverBaixo(self, mapa):
        if mapa[self.linha + 1][self.coluna] != '#':
            self.linha += 1