class Paredes:
    def __init__(self, mapa):
        self.mapa = mapa

    #Função que adiciona as paredes verticais no mapa
    def addLinhaVertical(self, coluna, linhaInicial, altura):
        for i in range(linhaInicial, linhaInicial + altura):
            self.mapa[i][coluna] = '#'
    

    def addLinhaHorizontal(self, linha, colunaInicial, largura):
        for i in range(colunaInicial, colunaInicial + largura):
            self.mapa[linha][i] = '#'

    def configurarMapa(paredes):
     #Linhas verticais do mapa
        paredes.addLinhaVertical(coluna=11, linhaInicial=1, altura=3)
        paredes.addLinhaVertical(coluna=6, linhaInicial=5, altura=10)
        paredes.addLinhaVertical(coluna=16, linhaInicial=5, altura=10)
        paredes.addLinhaVertical(coluna=11, linhaInicial=6, altura=2)
        paredes.addLinhaVertical(coluna=4, linhaInicial=7, altura=8)
        paredes.addLinhaVertical(coluna=18, linhaInicial=7, altura=8)
        paredes.addLinhaVertical(coluna=8, linhaInicial=10, altura=2)
        paredes.addLinhaVertical(coluna=14, linhaInicial=10, altura=2)
        paredes.addLinhaVertical(coluna=11, linhaInicial=15, altura=2)
        paredes.addLinhaVertical(coluna=4, linhaInicial=17, altura=2)
        paredes.addLinhaVertical(coluna=18, linhaInicial=17, altura=2)
        paredes.addLinhaVertical(coluna=6, linhaInicial=18, altura=2)
        paredes.addLinhaVertical(coluna=16, linhaInicial=18, altura=2)

    #Linhas horizontais do mapa
        paredes.addLinhaHorizontal(linha=2, colunaInicial=2, largura=3)
        paredes.addLinhaHorizontal(linha=3, colunaInicial=2, largura=3)
        paredes.addLinhaHorizontal(linha=2, colunaInicial=6, largura=4)
        paredes.addLinhaHorizontal(linha=3, colunaInicial=6, largura=4)
        paredes.addLinhaHorizontal(linha=2, colunaInicial=13, largura=4)
        paredes.addLinhaHorizontal(linha=3, colunaInicial=13, largura=4)
        paredes.addLinhaHorizontal(linha=2, colunaInicial=18, largura=3)
        paredes.addLinhaHorizontal(linha=3, colunaInicial=18, largura=3)
        paredes.addLinhaHorizontal(linha=5, colunaInicial=2, largura=3)
        paredes.addLinhaHorizontal(linha=5, colunaInicial=18, largura=3)
        paredes.addLinhaHorizontal(linha=5, colunaInicial=8, largura=7)
        paredes.addLinhaHorizontal(linha=7, colunaInicial=1, largura=4)
        paredes.addLinhaHorizontal(linha=14, colunaInicial=1, largura=4)
        paredes.addLinhaHorizontal(linha=7, colunaInicial=6, largura=4)
        paredes.addLinhaHorizontal(linha=7, colunaInicial=13, largura=4)
        paredes.addLinhaHorizontal(linha=7, colunaInicial=19, largura=4)
        paredes.addLinhaHorizontal(linha=14, colunaInicial=19, largura=4)
        paredes.addLinhaHorizontal(linha=9, colunaInicial=8, largura=7)
        paredes.addLinhaHorizontal(linha=12, colunaInicial=8, largura=7)
        paredes.addLinhaHorizontal(linha=14, colunaInicial=8, largura=7)
        paredes.addLinhaHorizontal(linha=16, colunaInicial=2, largura=3)
        paredes.addLinhaHorizontal(linha=16, colunaInicial=18, largura=3)
        paredes.addLinhaHorizontal(linha=16, colunaInicial=6, largura=4)
        paredes.addLinhaHorizontal(linha=16, colunaInicial=13, largura=4)
        paredes.addLinhaHorizontal(linha=18, colunaInicial=1, largura=2)
        paredes.addLinhaHorizontal(linha=18, colunaInicial=20, largura=2)
        paredes.addLinhaHorizontal(linha=18, colunaInicial=8, largura=7)
        paredes.addLinhaHorizontal(linha=18, colunaInicial=8, largura=7)
        paredes.addLinhaHorizontal(linha=20, colunaInicial=2, largura=8)
        paredes.addLinhaHorizontal(linha=20, colunaInicial=13, largura=8)











