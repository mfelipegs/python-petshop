from tkinter import *
from PIL import Image
tela = Tk()
import subprocess
from sys import platform
tela.title("Pet Shop's Dog's")
tela.resizable(True, True)
largura = 900
altura = 350

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

def abrir_tela_menu():
    subprocess.run([comando, "tela_inicial.py"])

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

opcoes_menus_menu.add_command(label="Home", command=abrir_tela_menu)
opcoes_menus_menu.add_command(label="Sair", command=tela.quit)

tela.config(menu=barra_menus)

pasta_inicial = ""

label_title = Label(tela, text="Cliente", padx=20, fg=fgColor, background=bgColor)
label_title.place(x=380, y=10)

label_nome = Label(tela, text="Nome", padx=2, fg=fgColor, background=bgColor)
label_nome.place(x=100, y=50)

txt_nome = Entry(tela, width=40, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_nome.place(x=100, y=75)


label_cpf = Label(tela, text="CPF", padx=2, fg=fgColor, background=bgColor)
label_cpf.place(x=440, y=50)

txt_cpf = Entry(tela, width=33, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_cpf.place(x=440, y=75)


label_celular = Label(tela, text="Celular", padx=2, fg=fgColor, background=bgColor)
label_celular.place(x=100, y=110)

txt_celular = Entry(tela, width=25, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_celular.place(x=100, y=135)


label_datanasc = Label(tela, text="Data de nasc.", padx=2, fg=fgColor, background=bgColor)
label_datanasc.place(x=325, y=110)

txt_datanasc = Entry(tela, width=18, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_datanasc.place(x=325, y=135)


label_end = Label(tela, text="Endereço", padx=2, fg=fgColor, background=bgColor)
label_end.place(x=500, y=110)

txt_end = Entry(tela, width=25, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_end.place(x=500, y=135)


label_cidade = Label(tela, text="Cidade", padx=2, fg=fgColor, background=bgColor)
label_cidade.place(x=100, y=170)

txt_cidade = Entry(tela, width=25, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_cidade.place(x=100, y=195)


label_estado = Label(tela, text="Estado", padx=2, fg=fgColor, background=bgColor)
label_estado.place(x=325, y=170)

txt_estado = Entry(tela, width=18, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_estado.place(x=325, y=195)


label_cep = Label(tela, text="CEP", padx=2, fg=fgColor, background=bgColor)
label_cep.place(x=500, y=170)

txt_cep = Entry(tela, width=25, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_cep.place(x=500, y=195)


btn_salvar = Button(tela, text="Salvar", width=10, bd=0, fg=textColor, bg=inputBgColor)
btn_salvar.place(x=600, y=250)


largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

tela.mainloop()