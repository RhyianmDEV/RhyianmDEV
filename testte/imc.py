import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        messagebox.showinfo("Resultado", f"Seu IMC é: {imc:.2f}")
        
        if imc < 18.5:
            interpretacao = "Você está abaixo do peso."
        elif 18.5 <= imc < 24.9:
            interpretacao = "Você está com peso normal."
        elif 25 <= imc < 29.9:
            interpretacao = "Você está com sobrepeso."
        else:
            interpretacao = "Você está com obesidade."
        
        messagebox.showinfo("Interpretação", interpretacao)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Configuração da janela principal
app = tk.Tk()
app.title("Calculadora de IMC")

# Labels e entradas para peso e altura
tk.Label(app, text="Peso (kg):").grid(row=0, column=0)
entry_peso = tk.Entry(app)
entry_peso.grid(row=0, column=1)

tk.Label(app, text="Altura (m):").grid(row=1, column=0)
entry_altura = tk.Entry(app)
entry_altura.grid(row=1, column=1)

# Botão para calcular o IMC
btn_calcular = tk.Button(app, text="Calcular IMC", command=calcular_imc)
btn_calcular.grid(row=2, columnspan=2)

# Inicia o loop principal da aplicação
app.mainloop()