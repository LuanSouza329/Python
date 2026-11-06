# API 002

Projeto em desenvolvimento para praticar a conexão de uma aplicação Python com
um banco de dados PostgreSQL. No estado atual, `main.py` tenta conectar ao banco
usando a classe `BancoDeDados`.

## Estrutura

```text
api002/
├── classes/
│   └── Database.py   # Configuração e acesso ao PostgreSQL
├── main.py           # Ponto de entrada
├── .env              # Configurações locais (não versionar)
└── .gitignore
```

## Requisitos

- Python 3
- PostgreSQL
- Pacotes Python `psycopg2` e `python-dotenv`

Instale os pacotes com:

```powershell
python -m pip install psycopg2-binary python-dotenv
```

## Configuração

Crie um arquivo `.env` nesta pasta, ao lado de `main.py`, com as configurações
do seu banco:

```dotenv
HOST_DB=localhost
DATA_BASE=nome_do_banco
USER_DB=seu_usuario
PASSWORD_DB=sua_senha
PORT_DB=5432
```

Não compartilhe nem versione o arquivo `.env`. O nome `PASSWORD_DB` deve
corresponder à variável lida em `classes/Database.py`.

## Execução

No PowerShell, entre na pasta `API\api002` e execute:

```powershell
python main.py
```

O import `from classes.Database import BancoDeDados` usado em `main.py` funciona
quando o comando é executado a partir desta pasta.

## Estado atual

O projeto ainda está incompleto: `executar_query()` não foi implementado, e a
chamada a `psycopg2.connect()` em `classes/Database.py` precisa receber o
parâmetro de senha com o valor carregado da configuração para conectar. A
conexão também é retornada por `conectar()`, mas não é armazenada em
`self.conexao`; portanto, `desconectar()` ainda não fecha essa conexão como o
código está escrito.
