import tkinter as tk


janela = tk.Tk()
janela.geometry('2000x1700')



text_teste = tk.Label(janela, text= 'ISSO É UM TEXTO',bg = 'yellow',fg='blue', font = ('roboto', 25))
text_teste.pack()


entry_text = tk.Entry(janela, bg = 'yellow',fg='blue', font = ('roboto', 25))
entry_text.pack()


btn =  tk.Button(janela, text = 'clique aqui', fg = 'green' ,bg = 'yellow',font = ('roboto', 25))
btn.pack()
janela.mainloop()