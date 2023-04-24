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

pasta_inicial = ""

label_title = Label(tela, text="Serviços - Novo atendimento", padx=20, fg=fgColor, background=bgColor)
label_title.place(x=380, y=10)

label_nome = Label(tela, text="CPF do cliente", padx=2, fg=fgColor, background=bgColor)
label_nome.place(x=100, y=50)

txt_nome = Entry(tela, width=30, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_nome.place(x=100, y=75)


label_cpf = Label(tela, text="Nome do animal", padx=2, fg=fgColor, background=bgColor)
label_cpf.place(x=355, y=50)

txt_cpf = Entry(tela, width=28, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_cpf.place(x=355, y=75)


label_duracao = Label(tela, text="Duração", padx=2, fg=fgColor, background=bgColor)
label_duracao.place(x=600, y=50)

txt_duracao = Entry(tela, width=12, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_duracao.place(x=600, y=75)


label_descricao = Label(tela, text="Descrição", padx=2, fg=fgColor, background=bgColor)
label_descricao.place(x=100, y=110)

txt_descricao = Entry(tela, width=60, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_descricao.place(x=100, y=135)


label_horainicio = Label(tela, text="Horário de início", padx=2, fg=fgColor, background=bgColor)
label_horainicio.place(x=100, y=170)

txt_horainicio = Entry(tela, width=15, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_horainicio.place(x=100, y=195)


label_preco = Label(tela, text="Preço", padx=2, fg=fgColor, background=bgColor)
label_preco.place(x=240, y=170)

txt_preco = Entry(tela, width=15, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_preco.place(x=240, y=195)


btn_salvar = Button(tela, text="Salvar", width=10, bd=0, fg=textColor, bg=inputBgColor)
btn_salvar.place(x=600, y=250)


largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

tela.mainloop()