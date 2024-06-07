import urllib.request
from html.parser import HTMLParser

class StockDataParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_table_row = False
        self.current_data = {}
        self.stock_data = []

    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.in_table_row = True
            self.current_data = {}
        elif tag == 'a' and self.in_table_row:
            for name, value in attrs:
                if name == 'href':
                    self.current_data['href'] = value

    def handle_data(self, data):
        if self.in_table_row and data.strip():
            if 'company' not in self.current_data:
                self.current_data['company'] = data.strip()
            else:
                key = f"column{len(self.current_data)}"
                self.current_data[key] = data.strip()

    def handle_endtag(self, tag):
        if tag == 'tr':
            self.in_table_row = False
            if self.current_data:
                self.stock_data.append(self.current_data)
req = urllib.request.Request("https://br.advfn.com/bolsa-de-valores/bovespa/info", headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    html = response.read().decode()

parser = StockDataParser()
parser.feed(html)

def limpaLista(lista):
    i=0
    x=lista[i]
    while x!={'company': 'Nome', 'column1': 'Último', 'column2': 'Compra', 'column3': 'Venda', 'column4': 'Variação', 'column5': 'Variação %', 'column6': 'Hora'}:
        lista.pop(i)
        i=0
        x=lista[i]
    lista.pop(i)
    return lista

limpaLista(parser.stock_data)

for x in parser.stock_data:
    print(x)