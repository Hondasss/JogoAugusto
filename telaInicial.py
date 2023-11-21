import os 
import WConio2 as WConio2

#Classe base para as telas
class TelaBase:
    def limpar_tela(self):
        os.system('cls')

    def aguardar_tecla(self):
        input("Pressione Enter para continuar...")

#Tela inicial do jogo
class TelaInicial(TelaBase):
    def showTelaInicial(self, opcaoJogador):
        self.limpar_tela()

        #Impressão do título e opções
        print("__" * 30)
        print("__" * 30)
        print("__" + 22 * " " + "PAC MAN" + 27 * " " + "__")
        print("__" * 30)
        print("__    1 - Novo Jogo FÁCIL" + 33 * " " + "__")
        print("__    2 - Novo Jogo DIFÍCIL" + 31 * " " + "__")
        print("__    3 - High Scores" + 37 * " " + "__")
        print("__    4 - Sair" + 44 * " " + "__")
        print("__" + 56 * " " + "__")
        print("__    Digite sua opção:" + 35 * " " + "__")
        print("__" * 30)
        print("__" * 30)

        #Cursor no começo do CMD
        WConio2.gotoxy(24, 9)
        opcaoJogador = input()

        #Valida a entrada do jogador, sendo suas opções 1, 2, 3, 4
        while opcaoJogador not in ["1", "2", "3", "4"]:
            self.limpar_tela()
            print("__" * 30)
            print("__" * 30)
            print("__" + 22 * " " + "PAC MAN" + 27 * " " + "__")
            print("__" * 30)
            print("__    1 - Novo Jogo FÁCIL" + 39 * " " + "__")
            print("__    2 - Novo Jogo DIFÍCIL" + 39 * " " + "__")
            print("__    3 - High Scores" + 37 * " " + "__")
            print("__    4 - Sair" + 44 * " " + "__")
            print("__" + 56 * " " + "__")
            print("__    Digite sua opção:" + 35 * " " + "__")
            print("__" * 30)
            print("__" * 30)

            WConio2.gotoxy(24, 8)
            opcaoJogador = input()

        return opcaoJogador

#Tela para um novo jogo
class TelaNovoJogo(TelaBase):
    def mostrarNovoJogo(self):
        self.limpar_tela()

        #Solicita o nome do jogador
        print("__" * 30)
        print("__" * 30)
        print("__    Digite seu nome: " + 35 * " " + "__")
        for _ in range(6):
            print("__" + 56 * " " + "__")
        print("__" * 30)
        print("__" * 30)
        print("")
            
        WConio2.gotoxy(23, 2)

        nomeJogador = input()

        return nomeJogador

#Tela para exibir as pontuações mais altas
def ordenar_pontuacoes():
    try:
        with open('ranking.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        pontuacoes = []

        for linha in linhas:
            elementos = linha.strip().split()
            if len(elementos) == 2:
                nome, pontuacao = elementos
                pontuacoes.append((nome, int(pontuacao)))
            else:
                print(f"Erro na linha: {linha.strip()}")

        pontuacoesOrdenadas = sorted(pontuacoes, key=lambda item: item[1], reverse=True)

        return pontuacoesOrdenadas

    except FileNotFoundError:
        return []  

    except Exception as e:
        return f"Erro ao ordenar pontuações: {str(e)}"


class TelaHighScores(TelaBase):
    def mostrarHighscore(self):
        self.limpar_tela()

        pontuacoesOrdenadas = ordenar_pontuacoes()

        print("╔════════════════════════════════════════════════╗")
        print("║               MAIORES PONTUAÇÕES               ║")
        print("╠════════════════════════════════════════════════╣")

        if not pontuacoesOrdenadas:
            print("║                  Sem pontuações                ║")
        else:
            for i, (nome, pontuacao) in enumerate(pontuacoesOrdenadas, start=1):
                # Ajuste a formatação para garantir que os campos estejam alinhados corretamente
                print(f"║  {i}. {nome.ljust(20)}: {str(pontuacao).rjust(5)}{' ' * 16}║")

        print("╚════════════════════════════════════════════════╝")

        self.aguardar_tecla()


class TelaGameOver(TelaBase):
    def showGameOver(self):
        self.limpar_tela()

        #Impressão da tela de Game Over
        print("__" * 30)
        print("__" * 30)
        print("__" + 22 * " " + "GAME OVER" + 24 * " " + "__")
        print("__" * 30)
        print("__    1 - Tentar Novamente" + 32 * " " + "__")
        print("__    2 - Sair do Jogo" + 38 * " " + "__")
        print("__" + 56 * " " + "__")
        print("__    Digite sua opção:" + 35 * " " + "__")
        print("__" * 30)
        print("__" * 30)

        WConio2.gotoxy(24, 7)
        opcaoJogador = input()

        #Validar a entrada
        while opcaoJogador not in ["1", "2"]:
            self.limpar_tela()
            print("__" * 30)
            print("__" * 30)
            print("__" + 22 * " " + "GAME OVER" + 24 * " " + "__")
            print("__" * 30)
            print("__    1 - Tentar Novamente" + 32 * " " + "__")
            print("__    2 - Sair do Jogo" + 38 * " " + "__")
            print("__" + 56 * " " + "__")
            print("__    Digite sua opção:" + 35 * " " + "__")
            print("__" * 30)
            print("__" * 30)
            
            WConio2.gotoxy(24, 7)
            opcaoJogador = input()

        return opcaoJogador