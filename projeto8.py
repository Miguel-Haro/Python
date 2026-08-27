import tkinter as tk
from tkinter import *
import os
from time import strftime

root = tk.Tk()
root.title('Seu relógio digital')
root.geometry("600x320")
root.maxsize(600, 320)
root.minsize(600, 320)
root.configure(background='#000000')

def get_saudacao():
    nome_usuario = os.getlogin()
    nome.config(text='Olá, ' + nome_usuario)

def get_data():
    data_atual = strftime(' %A, %D %B %Y')
    data.config(text= data_atual)

def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text=hora_atual)
    horas.after(1000, get_horas)

margin = tk.Canvas(root, width=600, height=60, bg='#000000', bd=0, highlightthickness=0, relief='ridge')
margin.pack()

nome = Label(root, background='#000000', fg="#fff", font=('Montserrat', 25))
nome.pack()

data = Label(root, background='#000000', fg="#fff", font=('Montserrat', 20))
data.pack(pady=2)

horas = Label(root, background='#000000', fg="#0BC8E1", font=('Montserrat', 64, 'bold'))
horas.pack(pady=2)

get_saudacao()
get_data()
get_horas()

root.mainloop()