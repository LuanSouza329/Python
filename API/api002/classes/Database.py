import psycopg2
import os
from dotenv import load_dotenv
    
load_dotenv()

class BancoDeDados:
    database = os.getenv("DATA_BASE")
    host = os.getenv("HOST_DB")
    usuario = os.getenv("USER_DB")
    senha = os.getenv("PASSWORD_DB")
    porta = os.getenv("PORT_DB")
    
    def __init__(self):
        self.conexao = None

    @staticmethod
    def conectar():
        # Lógica para conectar ao banco de dados
        try:
            conexao = psycopg2.connect(
                host=BancoDeDados.host,
                database=BancoDeDados.database,
                user=BancoDeDados.usuario,
                password=BancoDeDados.senha,
                port=BancoDeDados.porta
            )
            print("Conexão com o PostgreSQL realizada com sucesso!")
            return conexao
        except Exception as erro:
            print(f"Erro ao conectar ao banco de dados: {erro}")
            return None

    def desconectar(self):
        # Lógica para desconectar do banco de dados
        if self.conexao:
            self.conexao.close()
            print("Conexão com o PostgreSQL encerrada.")

    def executar_query(self, query):
        # Lógica para executar uma query no banco de dados
        pass