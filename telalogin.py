import tkinter as tk

def clique_do_botao():
    usuario = entrada_usuario.get()
    senha = entrada_senha.get()
    if usuario == "seu_usuario" and senha == "sua_senha":
        label_resultado.config(text="Login bem-sucedido!")
    else:
        label_resultado.config(text="Login falhou. Tente novamente.")

janela = tk.Tk()
janela.title("Aplicativo")
janela.geometry("400x200")
janela.configure(bg="blue")

label = tk.Label(janela, text="Interface Gráfica Escura", bg="white")
label.pack(pady=20)

entrada_usuario = tk.Entry(janela, text="Nome de usuário")
entrada_usuario.pack(pady=10)

entrada_senha = tk.Entry(janela, text="Senha", show="*")
entrada_senha.pack(pady=10)

botao = tk.Button(janela, text="Login", command=clique_do_botao)
botao.pack()

label_resultado = tk.Label(janela, text="", fg="white", bg="black")
label_resultado.pack(pady=10)

janela.mainloop()
