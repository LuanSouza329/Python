from classes.Database import BancoDeDados

if __name__ == "__main__":
    db = BancoDeDados()
    conexao = db.conectar()

    if conexao:
        print("Banco conectado")
        db.desconectar()