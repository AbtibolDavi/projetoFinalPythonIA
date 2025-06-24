# Monitor de Ações da Bovespa com Python

![Status](https://img.shields.io/badge/Status-Concluído-4CAF50?style=for-the-badge)
![Linguagem](https://img.shields.io/badge/Linguagem-Python-3776AB?style=for-the-badge)
![Licença](https://img.shields.io/badge/Licença-MIT-orange?style=for-the-badge)

Este projeto consiste em uma aplicação de desktop que extrai dados de ações da Bovespa do portal ADVFN, os armazena em um banco de dados local e os exibe em uma interface gráfica com uma tabela e um gráfico.

---

## ✨ Funcionalidades

-   **Scraping de Dados:** Utiliza as bibliotecas `urllib` e `HTMLParser` para extrair informações de ações diretamente do site ADVFN.
-   **Armazenamento Local:** Salva os dados coletados em um banco de dados SQLite (`bovespa.db`), permitindo a persistência das informações.
-   **Interface Gráfica:** Apresenta os dados de forma clara em uma tabela usando a biblioteca `Tkinter`.
-   **Visualização Gráfica:** Plota um gráfico de barras com `Matplotlib`, comparando os preços de compra e venda para análise visual rápida.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi construído utilizando majoritariamente bibliotecas padrão do Python e algumas bibliotecas populares de ciência de dados.

-   **Linguagem:** Python 3.x
-   **Extração de Dados:** `urllib.request`, `HTMLParser` (Bibliotecas Padrão)
-   **Manipulação de Dados:** `Pandas`
-   **Banco de Dados:** `sqlite3` (Biblioteca Padrão)
-   **Interface Gráfica (GUI):** `Tkinter` (Biblioteca Padrão)
-   **Visualização de Dados:** `Matplotlib`

---

## 🚀 Como Executar o Projeto

Para executar a aplicação, você precisa seguir **dois passos**. Primeiro, execute o script de extração para criar o banco de dados. Depois, execute o script da interface para visualizar os dados.

**1. Clone o repositório:**

```bash
git clone https://github.com/AbtibolDavi/projetoFinalPythonIA.git
cd projetoFinalPythonIA
```

**2. (Opcional, mas recomendado) Crie um ambiente virtual:**

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**4. Execute o script de extração de dados:**
Este comando irá criar o arquivo `bovespa.db` na pasta do projeto.

```bash
python bovespa_data.py
```

**5. Execute a interface gráfica:**
Após o script anterior terminar, execute este comando para abrir a janela da aplicação.

```bash
python bovespa_gui.py
```

---

---

## 📝 Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

**Davi Israel Abtibol Carvalho**
