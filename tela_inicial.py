from tkinter import *
from PIL import Image
import subprocess
from sys import platform
tela = Tk()
tela.title("Pet Shop's Dog's")
tela.resizable(True, True)
largura = 1000
altura = 700

bgColor = "#252A34"
inputBgColor = "#414856"
fgColor = "white"
textColor = "#F0FEEC"
tela.configure(background=bgColor)

if platform == "linux":
    # linux
    comando = "python3"
elif platform == "win32":
    # Windows...
    comando = "python"

def abrir_tela_clientes():
    subprocess.run([comando, "cliente.py"])

def abrir_tela_servicos():
    subprocess.run([comando, "servicos.py"])

def abrir_tela_animais():
    subprocess.run([comando, "animais.py"])

barra_menus = Menu(tela)

opcoes_menus_menu = Menu(barra_menus)
opcoes_menus_gestao = Menu(barra_menus)
#opcoes_menus_clientes = Menu(barra_menus)
#opcoes_menus_servicos = Menu(barra_menus)
#opcoes_menus_animais = Menu(barra_menus)

barra_menus.add_cascade(label="Menu", menu=opcoes_menus_menu)
#barra_menus.add_cascade(label="Clientes", menu=opcoes_menus_clientes, command=abrir_tela_clientes)
#barra_menus.add_cascade(label="Serviços", menu=opcoes_menus_servicos, command=abrir_tela_servicos)
#barra_menus.add_cascade(label="Animais", menu=opcoes_menus_animais, command=abrir_tela_animais)
barra_menus.add_cascade(label="Gestão", menu=opcoes_menus_gestao)
opcoes_menus_gestao.add_command(label="Clientes", command=abrir_tela_clientes)
opcoes_menus_gestao.add_command(label="Animais", command=abrir_tela_animais)
opcoes_menus_gestao.add_command(label="Servicos", command=abrir_tela_servicos)

opcoes_menus_menu.add_command(label="Sair", command=tela.quit)

tela.config(menu=barra_menus)

foto_cli = PhotoImage(file=r"icones/cli.png")
foto_an = PhotoImage(file=r"icones/an.png")
foto_service = PhotoImage(file=r"icones/service.png")

btn_cli = Button(tela, text="Clientes", image=foto_cli, compound=TOP, command=abrir_tela_clientes).place(x=300, y=200)
btn_an = Button(tela, text="Animais", image=foto_an, compound=TOP, command=abrir_tela_animais).place(x=500, y=200)
btn_service = Button(tela, text="Serviços", image=foto_service, compound=TOP, command=abrir_tela_servicos).place(x=700, y=200)

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

tela.mainloop()