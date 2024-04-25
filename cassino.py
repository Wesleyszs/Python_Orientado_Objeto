import tkinter as tk
from tkinter import messagebox
import random

class JogoDeApostasGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Apostas")

        self.saldo = 0

        # Labels
        self.lbl_saldo = tk.Label(root, text="Saldo: R$ 0.00")
        self.lbl_saldo.pack()

        # Entrada para depositar
        self.lbl_deposito = tk.Label(root, text="Depositar:")
        self.lbl_deposito.pack()
        self.ent_deposito = tk.Entry(root)
        self.ent_deposito.pack()

        # Botão para depositar
        self.btn_depositar = tk.Button(root, text="Depositar", command=self.depositar)
        self.btn_depositar.pack()

        # Entrada para apostar
        self.lbl_aposta = tk.Label(root, text="Valor da Aposta:")
        self.lbl_aposta.pack()
        self.ent_aposta = tk.Entry(root)
        self.ent_aposta.pack()

        # Botões para escolher a cor
        self.btn_vermelho = tk.Button(root, text="Vermelho", command=lambda: self.apostar("vermelho"))
        self.btn_vermelho.pack(side="left", padx=10, pady=10)
        self.btn_azul = tk.Button(root, text="Azul", command=lambda: self.apostar("azul"))
        self.btn_azul.pack(side="right", padx=10, pady=10)
        self.btn_empate = tk.Button(root, text="Empate", command=lambda: self.apostar("empate"))
        self.btn_empate.pack(padx=10, pady=10)

        # Botão para sair
        self.btn_sair = tk.Button(root, text="Sair", command=root.quit)
        self.btn_sair.pack()

    def depositar(self):
        try:
            valor_deposito = float(self.ent_deposito.get())
        except ValueError:
            messagebox.showerror("Erro", "Valor de depósito inválido.")
            return

        if valor_deposito <= 0:
            messagebox.showerror("Erro", "Valor de depósito inválido.")
            return

        self.saldo += valor_deposito
        self.lbl_saldo.config(text=f"Saldo: R$ {self.saldo:.2f}")
        messagebox.showinfo("Depósito", f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.")

    def apostar(self, cor):
        try:
            valor_aposta = float(self.ent_aposta.get())
        except ValueError:
            messagebox.showerror("Erro", "Valor de aposta inválido.")
            return

        if valor_aposta <= 0:
            messagebox.showerror("Erro", "Valor de aposta inválido.")
            return

        if valor_aposta > self.saldo:
            messagebox.showerror("Erro", "Saldo insuficiente para fazer a aposta.")
            return

        dado_vermelho = random.randint(1, 6)
        dado_azul = random.randint(1, 6)

        resultado = f"Resultado do dado vermelho: {dado_vermelho}\nResultado do dado azul: {dado_azul}\n\n"

        if dado_vermelho == dado_azul:
            self.saldo -= valor_aposta
            resultado += f"Empate! Você perdeu a aposta. Seu saldo atual é: R$ {self.saldo:.2f}"
        elif (cor == "vermelho" and dado_vermelho > dado_azul) or (cor == "azul" and dado_azul > dado_vermelho):
            self.saldo += valor_aposta
            resultado += f"Parabéns! Você acertou a cor {cor}. Seu saldo atual é: R$ {self.saldo:.2f}"
        else:
            self.saldo -= valor_aposta
            resultado += f"Que pena! Você errou a cor. Seu saldo atual é: R$ {self.saldo:.2f}"

        self.lbl_saldo.config(text=f"Saldo: R$ {self.saldo:.2f}")
        messagebox.showinfo("Resultado da Aposta", resultado)

def main():
    root = tk.Tk()
    app = JogoDeApostasGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
