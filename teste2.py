import requests
import webbrowser
import time
import tkinter as tk


def tela_dados(nome_entry):
    nome = nome_entry.get()
    pokemon = Pokemon(nome, '', '', '', '', ' ', '', '', '')
    pokemon.informacoes()
    pokemon_string = str(pokemon)
    print(text=pokemon_string)


class Pokemon:
    def __init__(self, nome, tipo, descricao, ataquebase, defesabase, ataqueespecial, defesaespecial, velocidade, peso):
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.ataque_base = ataquebase
        self.defesa_base = defesabase
        self.ataque_especial = ataqueespecial
        self.defesa_especial = defesaespecial
        self.velocidade = velocidade
        self.peso = peso

    def __str__(self):
        return f"Nome: {self.nome} Tipo: {self.tipo} Ataque Base: {self.ataque_base} Defesa Base: {self.defesa_base} Ataque Especial: {self.ataque_especial} Defesa Especial: {self.defesa_especial} Velocidade: {self.velocidade} Peso: {self.peso}"

    def informacoes(self):
        api = f'https://pokeapi.co/api/v2/pokemon/{self.nome}'
        res = requests.get(api)
        if res.status_code == 200:
            dados_pokemon = res.json()
            self.tipo = dados_pokemon['types'][0]['type']['name']
            self.ataque_base = dados_pokemon['stats'][1]['base_stat']
            self.defesa_base = dados_pokemon['stats'][2]['base_stat']
            self.ataque_especial = dados_pokemon['stats'][3]['base_stat']
            self.defesa_especial = dados_pokemon['stats'][4]['base_stat']
            self.velocidade = dados_pokemon['stats'][5]['base_stat']
            self.peso = dados_pokemon['weight']
        else:
            print(text=f"Não temos informações do pokemon: {self.nome}.")


class App:
    def __init__(self, master):
        master.geometry("400x250")
        master.title("Banco de Dados do Pokémon")

        frame = tk.Frame(master)
        frame.pack()

        bem_vindo_label = tk.Label(frame, text="Bem vindo ao Banco de Dados do Pokémon",
                                   font=('Helvetica', 14, 'bold'))
        bem_vindo_label.pack(pady=10)

        nome_label = tk.Label(frame, text="Nome do Pokémon:")
        nome_label.pack(pady=5)

        nome_entry = tk.Entry(frame)
        nome_entry.pack(pady=5)

        botao_pesquisar = tk.Button(frame, text="Pesquisar", command=lambda: tela_dados(nome_entry),
                                    font=('Helvetica', 12), bg='#ffd633', fg='white', bd=0, padx=10, pady=7)
        botao_pesquisar.pack(pady=10)

        botao_lista = tk.Button(frame, text="Ver a Lista de Pokémons Existentes", command=lambda: webbrowser.open(
            'https://psverso.com.br/listas/lista-todos-pokemon/'), font=('Helvetica', 12), bg='#ff3300', fg='white', bd=0,
                                padx=10, pady=7)
        botao_lista.pack(pady=10)

        botao_desenvolvedor = tk.Button(frame, text="Desenvolvedor", command=lambda: webbrowser.open(
            'https://github.com/nevesntc'), font=('Helvetica', 12)),
Pokemon.tela_dados()