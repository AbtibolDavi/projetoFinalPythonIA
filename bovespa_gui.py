import pandas as pd
import sqlite3
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('bovespa.db')

# Lê os dados da tabela bovespa para um DataFrame
df_bovespa = pd.read_sql_query("SELECT * FROM bovespa", conn)

# Fecha a conexão com o banco de dados
conn.close()

# Cria a janela principal do Tkinter
root = tk.Tk()
root.title("Dados da BOVESPA")

# Cria um frame para conter a tabela e o gráfico
frame_table = tk.Frame(root)
frame_table.pack(fill=tk.BOTH, expand=True)

# Cria a treeview para exibir os dados da tabela
tree = ttk.Treeview(frame_table)

# Define as colunas da treeview com base nas colunas do DataFrame
tree['columns'] = list(df_bovespa.columns)
# Mostra apenas os cabeçalhos das colunas
tree['show'] = 'headings'

# Define os cabeçalhos das colunas
for column in tree['columns']:
    tree.heading(column, text=column)

# Insere os dados do DataFrame na treeview
for index, row in df_bovespa.iterrows():
    tree.insert('', 'end', values=list(row))

# Empacota a treeview para ocupar o espaço do frame
tree.pack(fill=tk.BOTH, expand=True)

# Cria a figura e o eixo do gráfico matplotlib
fig, ax = plt.subplots(figsize=(12, 6))

# Plota um gráfico de barras das colunas Compra e Venda
df_bovespa[['Compra', 'Venda']].plot(kind='bar', ax=ax, title='Compra e venda na BOVESPA')

# Define os rótulos do eixo x como os valores da coluna Nome
ax.set_xticks(range(len(df_bovespa['Nome'])))
ax.set_xticklabels(df_bovespa['Nome'], rotation=45, ha='right')

# Ajusta o layout do gráfico para evitar sobreposição
plt.tight_layout()

# Cria um canvas para exibir o gráfico
canvas = FigureCanvasTkAgg(fig, master=frame_table)
# Adiciona uma barra de ferramentas ao gráfico
NavigationToolbar2Tk(canvas)
# Obtem o widget do canvas e empacota no frame
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
# Desenha o grafico no canvas
canvas.draw()

# Inicia o loop principal do Tkinter
root.mainloop()
