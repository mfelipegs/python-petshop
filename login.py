from tkinter import *
tela = Tk()
tela.title("Pet Shop's Dog's")
tela.resizable(True, True)
largura = 400
altura = 220

bgColor = "#252A34"
inputBgColor = "#414856"
fgColor = "white"
textColor = "#F0FEEC"
tela.configure(background=bgColor)

#for label in Label():
#    label.configure({"foreground": fgColor})

label_title = Label(tela, text="Bem-vindo!", padx=20, fg=fgColor, background=bgColor)
label_title.place(x=140, y=10)

label_usuario = Label(tela, text="Usuário", padx=2, fg=fgColor, background=bgColor)
label_usuario.place(x=100, y=50)

txt_usuario = Entry(tela, width=30, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_usuario.place(x=100, y=75)
#txt_usuario.configure({"background": InputBgColor})

label_senha = Label(tela, text="Senha", padx=2, fg=fgColor, background=bgColor)
label_senha.place(x=100, y=100)

txt_senha = Entry(tela, width=30, bd=0, fg=textColor, bg=inputBgColor, show="*")
txt_senha.place(x=100, y=125)
#txt_senha.configure({"background": InputBgColor})
#txt_senha.insert(0, "")

btn_logar = Button(tela, text="Entrar", width=19, bd=0, fg=textColor, bg=inputBgColor)
btn_logar.place(x=120, y=175)


largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

tela.mainloop()