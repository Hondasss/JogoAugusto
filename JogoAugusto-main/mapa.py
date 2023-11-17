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
        self.FantasmaAnterior = {
            "LinhaFantasma1": 0,
            "ColunaFantasma1": 0,
            "LinhaFantasma2": 0,
            "ColunaFantasma2": 0,
            "LinhaFantasma3": 0,
            "ColunaFantasma3": 0,
            "LinhaFantasma4": 0,
            "ColunaFantasma4": 0
        }
            

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

    def atualizaFantasma(self, fantasmas):
        for i in range(len(fantasmas)):
            self.limparPosicao(self.FantasmaAnterior[f"LinhaFantasma{i+1}"],
                               self.FantasmaAnterior[f"ColunaFantasma{i+1}"])
            f = fantasmas[i]
            self.plano[f.linha][f.coluna] = f.fantasma;
            self.FantasmaAnterior[f"LinhaFantasma{i+1}"] = f.linha
            self.FantasmaAnterior[f"ColunaFantasma{i+1}"] = f.coluna
            
    def limparPosicao(self, linha,  coluna):
        # Limpa a posição anterior do Pacman para dar impressao de movimento
        self.plano[linha][coluna] = ' '

    def imprimir(self): #Impressão
        for linha in self.plano:
            for caractere in linha:
                print(caractere, end=' ')
            print()
