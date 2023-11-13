class Pacman:
    def __init__(self, teste):
        self.teste = teste

    def imprimirTeste (self):
        return f"Olá, {self.teste}!"
    
pessoa1 = Pacman("João")
print(pessoa1.imprimirTeste())