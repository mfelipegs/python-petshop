from tkinter import *
from PIL import Image, ImageTk
tela = Tk()
tela.title("Pet Shop's Dog's")
tela.resizable(True, True)
largura = 800
altura = 400

bgColor = "#252A34"
inputBgColor = "#414856"
fgColor = "white"
textColor = "#F0FEEC"
tela.configure(background=bgColor)

pasta_inicial = ""

label_title = Label(tela, text="Cliente", padx=20, fg=fgColor, background=bgColor)
label_title.place(x=380, y=10)

label_nome = Label(tela, text="Usuário", padx=2, fg=fgColor, background=bgColor)
label_nome.place(x=100, y=50)

txt_nome = Entry(tela, width=40, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_nome.place(x=100, y=75)

label_cpf = Label(tela, text="CPF", padx=2, fg=fgColor, background=bgColor)
label_cpf.place(x=100, y=100)

txt_nome = Entry(tela, width=40, bd=0, fg=textColor, bg=inputBgColor, takefocus=0)
txt_nome.place(x=100, y=125)

largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
print(largura_screen, altura_screen)
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

tela.mainloop()