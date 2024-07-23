import tkinter as tk
from tkinter import ttk
from functions import acorde_maior, acorde_menor, acordes_maiores, acordes_menores

class OutraInformacao(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(sticky="nsew")
        self.criar_widgets()

    def criar_widgets(self):
        # Configuração do ComboBox para escolher a nota
        self.label_nota = tk.Label(self, text="Escolha a nota:")
        self.label_nota.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.combobox_nota = ttk.Combobox(self, values=self.obter_notas())
        self.combobox_nota.grid(row=0, column=1, padx=10, pady=10)

        # Configuração da caixa de seleção para escolher entre maior e menor
        self.label_tipo = tk.Label(self, text="Tipo de acorde:")
        self.label_tipo.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.tipo_acorde = tk.StringVar()
        self.tipo_acorde.set("Maior")  # Valor padrão
        self.checkbox_maior = tk.Radiobutton(self, text="Maior", variable=self.tipo_acorde, value="Maior")
        self.checkbox_maior.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.checkbox_menor = tk.Radiobutton(self, text="Menor", variable=self.tipo_acorde, value="Menor")
        self.checkbox_menor.grid(row=1, column=1, padx=10, pady=10, sticky="e")

        # Botão para exibir o acorde selecionado
        self.botao_exibir = tk.Button(self, text="Exibir Acorde", command=self.exibir_acorde)
        self.botao_exibir.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Label para exibir o resultado
        self.label_resultado = tk.Label(self, text="", font=("Helvetica", 12), justify="left")
        self.label_resultado.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="nsew")

    def obter_notas(self):
        # Função para obter a lista de notas musicais
        return ["Acordes", "A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]

    def exibir_acorde(self):
        nota = self.combobox_nota.get()
        tipo_acorde = self.tipo_acorde.get()

        if tipo_acorde == "Maior" and nota != "Acordes":
            resultado = self.formatar_acorde_maior(nota)
        elif tipo_acorde == "Maior" and nota == "Acordes":
            resultado = self.formatar_acordes_maiores()
        elif tipo_acorde == "Menor" and nota != "Acordes":
            resultado = self.formatar_acorde_menor(nota)
        elif tipo_acorde == "Menor" and nota == "Acordes":
            resultado = self.formatar_acorde_maior()

        self.label_resultado.config(text=resultado)
        self.botao_exibir.focus_set()  # Configura o foco para o botão "Exibir Acorde"

    def formatar_acorde_maior(self, nota):
        resultado = acorde_maior(nota)
        return resultado

    def formatar_acorde_menor(self, nota):
        resultado = acorde_menor(nota)
        return resultado
    
    def formatar_acordes_menores(self):
        resultado = acordes_menores()
        return resultado
    
    def formatar_acordes_maiores(self):
        resultado = acordes_maiores()
        return resultado

def iniciar_interface():
    root = tk.Tk()
    root.title("Outra Informação")
    app = OutraInformacao(master=root)
    app.mainloop()

if __name__ == "__main__":
    iniciar_interface()
