# 🍿 PopQuery - Sistema de Gerenciamento de Cinema

Projeto final da disciplina de Banco de Dados 1 do curso de Engenharia de Computação da Universidade Federal de Santa Catarina (UFSC).

## 🧑‍💻 Autores

- Saymon Martins Poli
- Yasmim Tezza Bardini
- Ananda Muxfeldt Palma

## 📝 Descrição

O PopQuery é um sistema de gerenciamento para uma rede de cinemas, desenvolvido em Python e integrado a um banco de dados PostgreSQL. O sistema oferece funcionalidades completas de CRUD, geração de relatórios analíticos e um sistema de recomendação de filmes baseado em IA com o Google Gemini.

O projeto foi construído utilizando Docker para facilitar a configuração e a execução do ambiente de banco de dados.

## ✨ Funcionalidades Principais

- **Gerenciamento de Dados (CRUD)**: Interface de linha de comando para inserir, consultar, atualizar e deletar registros de todas as tabelas do banco de dados (Filmes, Clientes, Sessões, etc.).
- **Relatórios Analíticos**: Geração de relatórios tabulares e gráficos, incluindo:
  - Top 5 filmes de maior bilheteria.
  - Análise de faturamento por dia da semana.
  - Correlação entre a nota do IMDb e o número de ingressos vendidos.
- **Recomendação com IA**: Um sistema que utiliza o Google Gemini para gerar recomendações de filmes personalizadas para os clientes com base em seu histórico de compras.
- **Administração do Banco de Dados**: Funções para criar, popular e deletar todas as tabelas do banco de dados de forma segura através do menu principal.

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3
- **Banco de Dados**: PostgreSQL
- **Ambiente**: Docker e Docker Compose
- **IA Generativa**: Google Gemini
- **Bibliotecas Python**: `psycopg2-binary`, `python-dotenv`, `google-generativeai`, `matplotlib`, `pandas`

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o projeto.

### 1. Pré-requisitos

- [Docker](https://www.docker.com/get-started) e [Docker Compose](https://docs.docker.com/compose/install/) instalados.
- [Python 3](https://www.python.org/downloads/) instalado.
- Acesso a uma chave de API do **Google Gemini**.

### 2. Configuração do Ambiente

**a. Clone o Repositório**
```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_DIRETORIO>
```

**b. Crie o Arquivo de Ambiente (`.env`)**

Crie um arquivo chamado `.env` na raiz do projeto. Ele deve conter as credenciais do banco de dados e a sua chave da API do Gemini. Use o exemplo abaixo:

```ini
# Credenciais do Banco de Dados PostgreSQL
POSTGRES_USER=myuser
POSTGRES_PASSWORD=mypassword
POSTGRES_NAME=cinema_db

# Chave da API do Google Gemini
GEMINI_KEY=SUA_CHAVE_DE_API_AQUI
```

**c. Inicie o Banco de Dados com Docker**

Execute o comando abaixo para iniciar o contêiner do PostgreSQL em segundo plano:

```bash
docker-compose up -d
```
Para verificar se o contêiner está rodando, use `docker-compose ps`.

**d. Instale as Dependências do Python**

Crie um ambiente virtual (recomendado) e instale as bibliotecas listadas no `requirements.txt`:

```bash
# Crie um ambiente virtual (opcional, mas recomendado)
python3 -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

# Instale as dependências
pip install -r requirements.txt
```

### 3. Execução e Inicialização do Banco

**a. Execute a Aplicação Principal**

Com o ambiente configurado, inicie o programa:

```bash
python3 main.py
```

**b. Inicialize o Banco de Dados pelo Menu**

Na primeira vez que executar o projeto, o banco de dados estará vazio. Use as opções do menu para inicializá-lo na ordem correta:

1.  Escolha a opção **`[11] Criar Tabelas`** para executar o script `CREATE TABLE` e criar toda a estrutura do banco.
2.  Depois, escolha a opção **`[10] Popular Banco`** para inserir os dados iniciais.

Após esses dois passos, o banco de dados estará pronto e você poderá utilizar todas as outras funcionalidades do sistema.

## 📂 Estrutura do Projeto

```
/
├── docker-compose.yml    # Configuração do serviço do PostgreSQL
├── main.py               # Ponto de entrada da aplicação, menu principal
├── requirements.txt      # Dependências do Python
├── sql/
│   ├── create_tables.sql # Schema do banco de dados (DDL)
│   └── populate_cinema.sql # Dados iniciais (DML)
├── src/
│   ├── connection.py     # Lógica de conexão com o banco
│   ├── crud.py           # Funções de Create, Read, Update e Delete
│   ├── db_admin.py       # Funções de administração (criar, popular, deletar tabelas)
│   ├── reports.py        # Funções para gerar relatórios tabulares
│   ├── grafic.py         # Funções para gerar gráficos a partir dos relatórios
│   └── ai.py             # Lógica para a recomendação com IA
└── .env                  # Arquivo para variáveis de ambiente (NÃO versionado)
```
