from tkinter import Tk

r = Tk()
teste = r.selection_get (selection = "CLIPBOARD")
print(teste)
r.destroy()