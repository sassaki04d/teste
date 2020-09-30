import os
from PIL import  Image as PILImage, ImageFilter
import tkinter
from tkinter import filedialog, messagebox, ttk
from time import time

window = tkinter.Tk()
window.title("Sassaconverter V0.1")
window.geometry('450x100')
window.configure(bg='light grey')
lbl_orig = ttk.Label(window,text='Pasta de Origem:')
lbl_orig.config(background='light grey')
lbl_orig.grid(row=1,column=1,padx=5,pady=5)
lbl_dest = ttk.Label(window,text='Pasta de Destino:')
lbl_dest.config(background='light grey')
lbl_dest.grid(row=2,column=1)
txt_orig = ttk.Entry(window,background = 'grey', width=45)
txt_orig.grid(row=1,column=2)
txt_dest = ttk.Entry(window,background = 'grey', width=45)
txt_dest.grid(row=2,column=2)
window.mainloop()
btn_orig = ttk.Button(window,text="Escolher Pasta",command=messagebox.showinfo('Teste','Botao pressionado!'))
btn_orig.pack()
btn_orig.grid(row=1,column=3)