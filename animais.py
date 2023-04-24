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

var = StringVar()
var.set("m")

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

label_title = Label(tela, text="Novo animal", padx=20, fg=fgColor, background=bgColor)
label_title.place(x=380, y=10)

label_cpf = Label(tela, text="CPF do Cliente", padx=2, fg=fgColor, background=bgColor)
label_cpf.place(x=100, y=50)

txt_cpf = Entry(tela, width=40, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_cpf.place(x=100, y=75)


label_nome = Label(tela, text="Nome do animal", padx=2, fg=fgColor, background=bgColor)
label_nome.place(x=440, y=50)

txt_nome = Entry(tela, width=33, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_nome.place(x=440, y=75)


label_deficiencia = Label(tela, text="Deficiências", padx=2, fg=fgColor, background=bgColor)
label_deficiencia.place(x=100, y=110)

txt_deficiencia = Entry(tela, width=40, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_deficiencia.place(x=100, y=135)


label_intolerancia = Label(tela, text="Intolerâncias", padx=2, fg=fgColor, background=bgColor)
label_intolerancia.place(x=440, y=110)

txt_intolerancia = Entry(tela, width=33, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_intolerancia.place(x=440, y=135)


label_datanasc = Label(tela, text="Dt. de Nascimento", padx=2, fg=fgColor, background=bgColor)
label_datanasc.place(x=100, y=170)

txt_datanasc = Entry(tela, width=22, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_datanasc.place(x=100, y=195)


label_idade = Label(tela, text="Idade aprox. (anos)", padx=2, fg=fgColor, background=bgColor)
label_idade.place(x=300, y=170)

txt_idade_anos = Entry(tela, width=15, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_idade_anos.place(x=300, y=195)


label_idade_meses = Label(tela, text="Idade aprox. (meses)", padx=2, fg=fgColor, background=bgColor)
label_idade_meses.place(x=440, y=170)

txt_idade_meses = Entry(tela, width=15, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_idade_meses.place(x=440, y=195)


label_sexo = Label(tela, text="Sexo", padx=2, fg=fgColor, background=bgColor)
label_sexo.place(x=600, y=170)

rdb_buttonm = Radiobutton(tela, text="M", variable=var, value="m", bg=inputBgColor)
rdb_buttonf = Radiobutton(tela, text="F", variable=var, value="f", bg=inputBgColor)
rdb_buttonm.place(x=600, y=195)
rdb_buttonf.place(x=650, y=195)


btn_salvar = Button(tela, text="Salvar", width=10, bd=0, fg=textColor, bg=inputBgColor)
btn_salvar.place(x=600, y=250)


largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

tela.mainloop()