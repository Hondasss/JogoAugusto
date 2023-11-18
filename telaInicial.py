import os 
import WConio2 as WConio2
from arquivos import *

# Classe base para as telas
class TelaBase:
    def limpar_tela(self):
        os.system('cls')

    def aguardar_tecla(self):
        input("Pressione Enter para continuar...")

# Tela inicial do jogo
class TelaInicial(TelaBase):
    def mostrar_tela_inicial(self, opcao_jogador):
        self.limpar_tela()

        # Impressão do título e opções
        print("__" * 30)
        print("__" * 30)
        print("__" + 22 * " " + "PAC MAN" + 27 * " " + "__")
        print("__" * 30)
        print("__    1 - Novo Jogo" + 39 * " " + "__")
        print("__    2 - High Scores" + 37 * " " + "__")
        print("__    3 - Sair" + 44 * " " + "__")
        print("__" + 56 * " " + "__")
        print("__    Digite sua opção:" + 35 * " " + "__")
        print("__" * 30)
        print("__" * 30)

        # Posicionar o cursor na tela
        WConio2.gotoxy(24, 8)
        opcao_jogador = input()

        # Validar a entrada do jogador
        while opcao_jogador not in ["1", "2", "3"]:
            self.limpar_tela()
            print("__" * 30)
            print("__" * 30)
            print("__" + 22 * " " + "PAC MAN" + 27 * " " + "__")
            print("__" * 30)
            print("__    1 - Novo Jogo" + 39 * " " + "__")
            print("__    2 - High Scores" + 37 * " " + "__")
            print("__    3 - Sair" + 44 * " " + "__")
            print("__" + 56 * " " + "__")
            print("__    Digite sua opção:" + 35 * " " + "__")
            print("__" * 30)
            print("__" * 30)

            # Posicionar o cursor na tela
            WConio2.gotoxy(24, 8)
            opcao_jogador = input()

        return opcao_jogador

# Tela para um novo jogo
class TelaNovoJogo(TelaBase):
    def mostrar_tela_novo_jogo(self):
        self.limpar_tela()

        # Solicitar o nome do jogador
        print("__" * 30)
        print("__" * 30)
        print("__    Digite seu nome: " + 35 * " " + "__")
        for _ in range(6):
            print("__" + 56 * " " + "__")
        print("__" * 30)
        print("__" * 30)
        print("")
            
        # Posicionar o cursor na tela
        WConio2.gotoxy(23, 2)

        nome_jogador = input()

        return nome_jogador

# Tela para exibir as pontuações mais altas
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

        pontuacoes_ordenadas = sorted(pontuacoes, key=lambda item: item[1], reverse=True)

        return pontuacoes_ordenadas

    except FileNotFoundError:
        return []  

    except Exception as e:
        return f"Erro ao ordenar pontuações: {str(e)}"


class TelaHighScores(TelaBase):
    def mostrar_tela_high_scores(self):
        self.limpar_tela()

        pontuacoes_ordenadas = ordenar_pontuacoes()

        print("╔════════════════════════════════════════════════╗")
        print("║               MAIORES PONTUAÇÕES               ║")
        print("╠════════════════════════════════════════════════╣")

        if not pontuacoes_ordenadas:
            print("║                  Sem pontuações                ║")
        else:
            for i, (nome, pontuacao) in enumerate(pontuacoes_ordenadas, start=1):
                # Ajuste a formatação para garantir que os campos estejam alinhados corretamente
                print(f"║  {i}. {nome.ljust(20)}: {str(pontuacao).rjust(5)}{' ' * 16}║")

        print("╚════════════════════════════════════════════════╝")

        self.aguardar_tecla()


class TelaGameOver(TelaBase):
    def mostrar_tela_game_over(self):
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
        opcao_jogador = input()

        #Validar a entrad
        while opcao_jogador not in ["1", "2"]:
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
            opcao_jogador = input()

        return opcao_jogador