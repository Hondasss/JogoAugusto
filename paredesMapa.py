class Paredes:
    def __init__(self, mapa):
        self.mapa = mapa

    #Função que adiciona as paredes verticais no mapa
    def addLinhaVertical(self, coluna, linhaInicial, altura):
        for i in range(linhaInicial, linhaInicial + altura):
            self.mapa[i][coluna] = '\033[34;1m#\033[m'
    
    #Função que adiciona as paredes horizontais no mapa
    def addLinhaHorizontal(self, linha, colunaInicial, largura):
        for i in range(colunaInicial, colunaInicial + largura):
            self.mapa[linha][i] = '\033[34;1m#\033[m'

    def configurarMapa(paredes):
     #Linhas verticais do mapa
        paredes.addLinhaVertical(coluna=11, linhaInicial=1, altura=3)
        paredes.addLinhaVertical(coluna=6, linhaInicial=5, altura=10)
        paredes.addLinhaVertical(coluna=16, linhaInicial=5, altura=10)
        paredes.addLinhaVertical(coluna=11, linhaInicial=6, altura=2)
        paredes.addLinhaVertical(coluna=4, linhaInicial=7, altura=6)
        paredes.addLinhaVertical(coluna=18, linhaInicial=7, altura=6)
        paredes.addLinhaVertical(coluna=8, linhaInicial=10, altura=2)
        paredes.addLinhaVertical(coluna=14, linhaInicial=10, altura=2)
        paredes.addLinhaVertical(coluna=11, linhaInicial=15, altura=2)
        paredes.addLinhaVertical(coluna=4, linhaInicial=17, altura=2)
        paredes.addLinhaVertical(coluna=18, linhaInicial=17, altura=2)
        paredes.addLinhaVertical(coluna=6, linhaInicial=18, altura=2)
        paredes.addLinhaVertical(coluna=16, linhaInicial=18, altura=2)
        paredes.addLinhaVertical(coluna=20, linhaInicial=7, altura=6)
        paredes.addLinhaVertical(coluna=2, linhaInicial=7, altura=6)
        paredes.addLinhaVertical(coluna=0, linhaInicial=0, altura=1)

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
        paredes.addLinhaHorizontal(linha=14, colunaInicial=1, largura=4)
        paredes.addLinhaHorizontal(linha=7, colunaInicial=6, largura=4)
        paredes.addLinhaHorizontal(linha=7, colunaInicial=13, largura=4)
        paredes.addLinhaHorizontal(linha=14, colunaInicial=19, largura=4)
        paredes.addLinhaHorizontal(linha=9, colunaInicial=8, largura=3)
        paredes.addLinhaHorizontal(linha=9, colunaInicial=12, largura=3)
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
        paredes.addLinhaHorizontal(linha=0, colunaInicial=0, largura=1)


    def configurarMapa2(paredes):
    #Linhas verticais do mapa
        paredes.addLinhaVertical(coluna=11, linhaInicial=1, altura=3)
        paredes.addLinhaVertical(coluna=6, linhaInicial=5, altura=10)
        paredes.addLinhaVertical(coluna=16, linhaInicial=5, altura=10)
        paredes.addLinhaVertical(coluna=11, linhaInicial=6, altura=2)
        paredes.addLinhaVertical(coluna=4, linhaInicial=7, altura=6)
        paredes.addLinhaVertical(coluna=18, linhaInicial=7, altura=6)
        paredes.addLinhaVertical(coluna=8, linhaInicial=11, altura=1)
        paredes.addLinhaVertical(coluna=14, linhaInicial=11, altura=1)
        paredes.addLinhaVertical(coluna=11, linhaInicial=15, altura=2)
        paredes.addLinhaVertical(coluna=4, linhaInicial=17, altura=2)
        paredes.addLinhaVertical(coluna=18, linhaInicial=17, altura=2)
        paredes.addLinhaVertical(coluna=6, linhaInicial=18, altura=2)
        paredes.addLinhaVertical(coluna=16, linhaInicial=18, altura=2)
        paredes.addLinhaVertical(coluna=20, linhaInicial=7, altura=6)
        paredes.addLinhaVertical(coluna=2, linhaInicial=7, altura=6)
        paredes.addLinhaVertical(coluna=8, linhaInicial=4, altura=4)
        paredes.addLinhaVertical(coluna=14, linhaInicial=4, altura=4)
        paredes.addLinhaVertical(coluna=2, linhaInicial=18, altura=3)
        paredes.addLinhaVertical(coluna=20, linhaInicial=18, altura=3)
        paredes.addLinhaVertical(coluna=11, linhaInicial=2, altura=1)

    #Linhas horizontais do mapa
        paredes.addLinhaHorizontal(linha=2, colunaInicial=2, largura=8)    
        paredes.addLinhaHorizontal(linha=2, colunaInicial=13, largura=8) 
        paredes.addLinhaHorizontal(linha=5, colunaInicial=2, largura=3) 
        paredes.addLinhaHorizontal(linha=5, colunaInicial=18, largura=3) 
        paredes.addLinhaHorizontal(linha=3, colunaInicial=2, largura=7)  
        paredes.addLinhaHorizontal(linha=3, colunaInicial=14, largura=7) 
        paredes.addLinhaHorizontal(linha=9, colunaInicial=8, largura=3)     
        paredes.addLinhaHorizontal(linha=9, colunaInicial=12, largura=3) 
        paredes.addLinhaHorizontal(linha=11, colunaInicial=12, largura=3) 
        paredes.addLinhaHorizontal(linha=11, colunaInicial=8, largura=3) 
        paredes.addLinhaHorizontal(linha=13, colunaInicial=8, largura=3) 
        paredes.addLinhaHorizontal(linha=13, colunaInicial=12, largura=3) 
        paredes.addLinhaHorizontal(linha=14, colunaInicial=2, largura=3) 
        paredes.addLinhaHorizontal(linha=14, colunaInicial=18, largura=3)
        paredes.addLinhaHorizontal(linha=16, colunaInicial=4, largura=6)
        paredes.addLinhaHorizontal(linha=16, colunaInicial=13, largura=6)
        paredes.addLinhaHorizontal(linha=19, colunaInicial=6, largura=11)
        paredes.addLinhaHorizontal(linha=20, colunaInicial=3, largura=3)
        paredes.addLinhaHorizontal(linha=20, colunaInicial=17, largura=3)