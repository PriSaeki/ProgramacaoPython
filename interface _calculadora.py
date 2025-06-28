import tkinter as tk


def somar():
    numero1 = float(numero_1.get())
    numero2 = float(numero_2.get())
    result  = numero1 + numero2
    resultado.config(text = result)

def sub():
    numero1 = float(numero_1.get())
    numero2 = float(numero_2.get())
    result  = numero1 - numero2
    resultado.config(text = result)

def mult():
    numero1 = float(numero_1.get())
    numero2 = float(numero_2.get())
    result  = numero1 * numero2
    resultado.config(text = result)

def div():
    numero1 = float(numero_1.get())
    numero2 = float(numero_2.get())
    result  = numero1 / numero2
    resultado.config(text = result)


root = tk.Tk()
root.title('CALCULADORA')
root.geometry('600x400')
root.configure(bg = 'green')


tk.Label(root, text = 'CALCULADORA').grid(row = 0 , column=3)

tk.Label(root, text = 'N1: ', font=('roboto', 15)).grid(row = 1 , column=3, pady=10, padx=10)
numero_1 = tk.Entry(root, font=('roboto', 15))
numero_1.grid(row=2, column=3)


tk.Label(root, text = 'N2: ', font=('roboto', 15)).grid(row = 1 , column=4, pady=10, padx=10)
numero_2 = tk.Entry(root, font=('roboto', 15))
numero_2.grid(row=2, column=4)




btn_soma = tk.Button(root, text='soma', width=10, command=somar, font=('roboto', 15))
btn_soma.grid(row = 3, column=3, padx=10, pady=10)

btn_subtracao = tk.Button(root, text='subtracao', width=10, command=sub, font=('roboto', 15))
btn_subtracao.grid(row = 4, column=3, padx=10, pady=10)

btn_multiplicar = tk.Button(root, text='multiplicar', width=10, command=mult, font=('roboto', 15))
btn_multiplicar.grid(row = 5, column=3, padx=10, pady=10)

btn_divisao = tk.Button(root, text='divisao', width=10, command=div, font=('roboto', 15))
btn_divisao.grid(row = 6, column=3, padx=10, pady=10)



resultado = tk.Label(root, text = '=', font=('roboto', 15))
resultado.grid(row = 7 , column=0, pady=10, padx=10)


root.mainloop()