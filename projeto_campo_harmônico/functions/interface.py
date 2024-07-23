import tkinter as tk
from .reproducao_som import ReprodutorSom

class InterfacePiano:
    def __init__(self, root):
        self.root = root
       #self.root.title("Piano Virtual")
        self.reprodutor = ReprodutorSom()
        self.teclas_ativas = set()

        # Frame para o teclado virtual
        frame_teclado = tk.Frame(self.root, bg="white")
        frame_teclado.pack(pady=20)

        # Lista de teclas do piano
        teclas_piano = ["C3", "C3#", "D3", "D3#", "E3", "F3", "F3#", "G3", "G3#", "A3", "A3#", "B3",
                        "C4", "C4#", "D4", "D4#", "E4", "F4", "F4#", "G4", "G4#", "A4", "A4#", "B4",
                        "C5", "C5#", "D5", "D5#", "E5", "F5", "F5#", "G5", "G5#", "A5", "A5#", "B5"]

        # Mapeamento de teclas físicas para teclas do piano virtual
        self.mapeamento_teclas = {
            "q": "C3", "2": "C3#", "w": "D3", "3": "D3#", "e": "E3", "r": "F3", "5": "F3#",
            "t": "G3", "6": "G3#", "y": "A3", "7": "A3#", "u": "B3",
            "i": "C4", "9": "C4#", "o": "D4", "0": "D4#", "p": "E4", "[": "F4", "=": "F4#",
            "z": "G4", "s": "G4#", "x": "A4", "d": "A4#", "c": "B4",
            "v": "C5", "g": "C5#", "b": "D5", "h": "D5#", "n": "E5", "m": "F5", "k": "F5#",
            ",": "G5", "l": "G5#", ".": "A5", "ç": "A5#", ";": "B5"
        }
        # Criar botões para cada tecla do teclado
        self.botoes_teclas = {}
        posicao_coluna = 0
        for nota in teclas_piano:
            if nota.endswith("#"):  # Teclas pretas (sustenidas)
                cor = "#333333"  # Cinza escuro
                largura = 3
                altura = 10
                relief = "ridge"  # Relevo para simular a altura
                padx = (0, 1)  # Adiciona um pequeno espaço à direita para separar das teclas brancas
                pady = (0, 95)
                columnspan = 1  # Coluna única para teclas pretas
            else:  # Teclas brancas (naturais)
                cor = "#ffffff"  # Branco
                largura = 6
                altura = 16
                relief = "raised"  # Relevo para simular uma superfície elevada
                padx = (1, 0)  # Adiciona um pequeno espaço à esquerda para separar das teclas pretas
                pady = (0, 0)
                columnspan = 2  # Coluna dupla para teclas brancas
            
            # Ajusta a posição da próxima tecla
            btn = tk.Button(frame_teclado, text=nota, width=largura, height=altura, bg=cor, relief=relief, bd=1)
            btn.grid(row=0, column=posicao_coluna, columnspan=columnspan, padx=padx, pady=pady)
            self.botoes_teclas[nota] = btn
            
            if nota.endswith("#"):
                posicao_coluna += 1
            else:
                posicao_coluna += 2

        # Associar eventos de teclado
        self.root.bind("<KeyPress>", self.tecla_pressionada)
        self.root.bind("<KeyRelease>", self.tecla_liberada)
        self.root.focus_set()  # Focar a janela para capturar eventos de teclado

    def tecla_pressionada(self, event):
        tecla = event.keysym.lower()
        if tecla in self.mapeamento_teclas:
            nota = self.mapeamento_teclas[tecla]
            if nota not in self.teclas_ativas:
                self.teclas_ativas.add(nota)
                self.botoes_teclas[nota].config(bg="#cccccc")  # Mudar cor para simular pressionado
                self.reprodutor.tocar_nota(nota)

    def tecla_liberada(self, event):
        tecla = event.keysym.lower()
        if tecla in self.mapeamento_teclas:
            nota = self.mapeamento_teclas[tecla]
            if nota in self.teclas_ativas:
                self.teclas_ativas.remove(nota)
                if nota.endswith("#"):
                    self.botoes_teclas[nota].config(bg="#333333")  # Restaurar cor das teclas pretas
                else:
                    self.botoes_teclas[nota].config(bg="#ffffff")  # Restaurar cor das teclas brancas

def iniciar_interface():
    root = tk.Tk()
    app = InterfacePiano(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_interface()
