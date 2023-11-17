class Mapa:
    #Definição da função INIT, que armazenará variáveis de controle da largura e altura
    def __init__(self, largura, altura):
        #Iniciando altura e largura
        self.largura = largura 
        self.altura = altura

        #Iniciando uma matriz que representará toda a área do jogo, sendo essa ALTURA x LARGURA
        self.plano = [['.' for coluna in range(largura)] for linha in range(altura)] #O ponto representa o valor inicial de cada célula na matriz
        self.bordas() #O método é chamado aqui para criar as bordas desde o inicio do jogo, garantindo solidez e evitando erros
        self.linhaPacmanAnterior = 0  
        self.colunaPacmanAnterior = 0

        self.linhaFantasma1Anterior = 0
        self.colunaFantasma1Anterior = 0
        self.linhaFantasma2Anterior = 0
        self.colunaFantasma2Anterior = 0
        self.linhaFantasma3Anterior = 0
        self.colunaFantasma3Anterior = 0
        self.linhaFantasma4Anterior = 0
        self.colunaFantasma4Anterior = 0

    def bordas(self):
        #Método que adiciona as bordas delimitadas por #
        for i in range(self.largura):
            self.plano[0][i] = '#' #Tampa
            self.plano[self.altura - 1][i] = '#' #Fundo

        for i in range(self.altura):
            self.plano[i][0] = '#' #Lateral esquerda
            self.plano[i][self.largura - 1] = '#' #Lateral direita 

    def atualizaCaractere(self, caractere, linha, coluna):
        # Limpa a posição anterior do Pacman
        self.limparPosicao(self.linhaPacmanAnterior, self.colunaPacmanAnterior)

        # Proteção do script para verificação da linha e coluna dentro do limite máximo
        if 0 <= linha < self.altura and 0 <= coluna < self.largura:
            self.linhaPacmanAnterior, self.colunaPacmanAnterior = linha, coluna
            self.plano[linha][coluna] = caractere

    def atualizaFantasma1(self, caractere, linha, coluna):
        # Limpa a posição anterior do Fantasma
        self.limparPosicao(self.linhaFantasma1Anterior, self.colunaFantasma1Anterior)

        if 0 <= linha < self.altura and 0 <= coluna < self.largura:
            self.linhaFantasma1Anterior, self.colunaFantasma1Anterior = linha, coluna
            self.plano[linha][coluna] = caractere 

    def atualizaFantasma2(self, caractere, linha, coluna):
        # Limpa a posição anterior do Fantasma
        self.limparPosicao(self.linhaFantasma2Anterior, self.colunaFantasma2Anterior)

        if 0 <= linha < self.altura and 0 <= coluna < self.largura:
            self.linhaFantasma2Anterior, self.colunaFantasma2Anterior = linha, coluna
            self.plano[linha][coluna] = caractere

    def atualizaFantasma3(self, caractere, linha, coluna):
        # Limpa a posição anterior do Fantasma
        self.limparPosicao(self.linhaFantasma3Anterior, self.colunaFantasma3Anterior)

        if 0 <= linha < self.altura and 0 <= coluna < self.largura:
            self.linhaFantasma3Anterior, self.colunaFantasma3Anterior = linha, coluna
            self.plano[linha][coluna] = caractere

    def atualizaFantasma4(self, caractere, linha, coluna):
        # Limpa a posição anterior do Fantasma
        self.limparPosicao(self.linhaFantasma4Anterior, self.colunaFantasma4Anterior)

        if 0 <= linha < self.altura and 0 <= coluna < self.largura:
            self.linhaFantasma4Anterior, self.colunaFantasma4Anterior = linha, coluna
            self.plano[linha][coluna] = caractere

    def limparPosicao(self, linha,  coluna):
        # Limpa a posição anterior do Pacman e do Fantasma para dar impressao de movimento
        self.plano[linha][coluna] = ' '

    def imprimir(self): #Impressão
        for linha in self.plano:
            for caractere in linha:
                print(caractere, end=' ')
            print()
