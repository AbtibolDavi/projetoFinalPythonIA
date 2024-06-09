import urllib.request
from html.parser import HTMLParser
import pandas as pd
import sqlite3


# Classe personalizada de HTMLParser para analisar e extrair dados da tabela HTML
class AcoesParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table_row = False
        self.current_data = {}
        self.acoes = []

    # Método chamado quando uma tag de abertura é encontrada
    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.in_table_row = True
            self.current_data = {}
        elif tag == 'a' and self.in_table_row:
            for name, value in attrs:
                if name == 'href':
                    self.current_data['href'] = value

    # Método chamado quando dados entre tags são encontrados
    def handle_data(self, data):
        if self.in_table_row and data.strip():
            if 'company' not in self.current_data:
                self.current_data['company'] = data.strip()
            else:
                key = f"column{len(self.current_data)}"
                self.current_data[key] = data.strip()

    # Método chamado quando uma tag de fechamento é encontrada
    def handle_endtag(self, tag):
        if tag == 'tr':
            self.in_table_row = False
            if self.current_data:
                self.acoes.append(self.current_data)


# Função para converter preços de string para float
def converte_preco(preco_str):
    return float(preco_str.replace(',', '.'))


# Função para converter porcentagens de string para float
def converte_porcentagem(porcentagem_str):
    return float(porcentagem_str.replace('%', '').replace(',', '.'))


# Função para limpar e formatar a lista de dados extraídos
def limpa_lista(lista):
    i = 0
    x = lista[i]
    # Remover itens da lista até encontrar o cabeçalho da tabela
    while x != {'company': 'Nome', 'column1': 'Último', 'column2': 'Compra', 'column3': 'Venda', 'column4': 'Variação',
                'column5': 'Variação %', 'column6': 'Hora'}:
        lista.pop(i)
        i = 0
        x = lista[i]
    lista.pop(i)  # Remove o cabeçalho da lista
    lista.pop()  # Remove elemento duplicado
    lista_limpa = []
    # Limpar e converter cada item da lista
    for item in lista:
        item_limpo = {
            'Nome': item['company'],
            'Ultimo': converte_preco(item['column2']),
            'Compra': converte_preco(item['column3']),
            'Venda': converte_preco(item['column4']),
            'Variacao': converte_preco(item['column5']),
            'Variacao %': converte_porcentagem(item['column6']),
            'Hora': item['column7']
        }
        lista_limpa.append(item_limpo)
    return lista_limpa


# Solicita a página web com informações da Bovespa
req = urllib.request.Request("https://br.advfn.com/bolsa-de-valores/bovespa/info",
                             headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    html = response.read().decode()

# Análise do HTML e extração dos dados
parser = AcoesParser()
parser.feed(html)

print("Lista a partir do HTML inicial:")
for stock in parser.acoes:
    print(stock)

# Copia os dados extraídos para uma nova lista
bovespa = parser.acoes.copy()

# Limpa e formata os dados extraídos
bovespa = limpa_lista(bovespa)

# Cria um DataFrame a partir dos dados limpos
df = pd.DataFrame(bovespa)

print("DataFrame completo a partir da lista limpa do parsing:")
print(df)

# Conecta ao banco de dados SQLite e armazena o DataFrame
conn = sqlite3.connect('bovespa.db')
df.to_sql('bovespa', conn, if_exists='replace', index=False)
conn.commit()
conn.close()

# Lê os dados armazenados no banco de dados para um DataFrame
conn = sqlite3.connect('bovespa.db')
df_bd = pd.read_sql('SELECT * FROM bovespa', conn)
conn.close()

print("DataFrame completo a partir do banco de dados:")
print(df_bd)
