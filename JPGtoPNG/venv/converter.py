import os
from PIL import  Image as PILImage, ImageFilter
import tkinter as tk
from tkinter import filedialog, messagebox
from time import time
root = tk.Tk()
root.withdraw()
while True:

    messagebox.showinfo('Aviso!','Selecione a pasta de origem para converter os arquivos JPG em PNG.')
    origem = filedialog.askdirectory()
    if origem == '':
        messagebox.showerror('Erro!', 'Operação cancelada!\nAbortando programa!')
        exit()
    else:
        break

while True:

    messagebox.showinfo('Aviso!','Selecione a pasta de destino para salvar os arquivos PNG.')
    destino = filedialog.askdirectory()
    if destino == '':
        messagebox.showerror('Erro!', 'Operação cancelada!\nAbortando programa!')
        exit()
    else:
        break

time1 = time()
ct = 0
for filename in os.listdir(origem):
    path = os.path.join(origem,filename)
    extensao = os.path.splitext(filename)[1]
    if not os.path.isdir(path) and (extensao == '.jpg' or extensao == '.JPG'):
        img: PILImage.Image = PILImage.open(f'{origem}/{filename}')
        img.thumbnail((1000,1000))
        img = img.convert('LA')
        novonome = os.path.splitext(filename)[0]
        novonome = destino+'/'+novonome+'.png'
        img.save(novonome,'png')
        ct+=1
        if ct > 10:
            break
time2 = time()
total = time2-time1
messagebox.showinfo(f'Arquivos convertidos com sucesso.',f'Foram convertidos {ct} arquivos no total.\nTempo de execução: {total}s')