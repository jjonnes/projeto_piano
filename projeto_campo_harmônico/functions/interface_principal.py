import tkinter as tk
from .interface import InterfacePiano
from .outra_informacao import OutraInformacao

class InterfacePrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Piano Virtual")

        # Frame para o piano (parte superior)
        frame_piano = tk.Frame(self.root, bg="white")
        frame_piano.pack(fill=tk.BOTH, expand=True)

        # Instanciar o piano virtual dentro do frame_piano
        self.piano = InterfacePiano(frame_piano)

        # Frame para outras informações (parte inferior)
        frame_informacao = tk.Frame(self.root, bg="lightgray", padx=20, pady=10)
        frame_informacao.pack(fill=tk.BOTH, expand=True)

        # Instanciar as outras informações dentro do frame_informacao
        self.outra_informacao = OutraInformacao(frame_informacao)

        # Focar o frame do piano ao clicar em qualquer lugar da janela
        self.root.bind("<Button-1>", lambda event: frame_piano.focus_set())

def iniciar_interface():
    root = tk.Tk()
    app = InterfacePrincipal(root)
    root.mainloop()

if __name__ == "__main__":
    iniciar_interface()
