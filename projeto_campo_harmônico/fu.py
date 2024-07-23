import tkinter as tk
import functions

root = tk.Tk()  # Crie a instância principal do Tkinter
piano = functions.InterfacePrincipal(root)  # Passe root como argumento para InterfacePiano
root.mainloop()

