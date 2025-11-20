import os
import psycopg2

# -----------------------------------------------------------------
# FUNÇÃO DE CONEXÃO (Item a)
# -----------------------------------------------------------------
def connect_popquery():
    """
    Se conecta ao banco de dados PostgreSQL usando as 
    variáveis salvas no arquivo .env.
    Retorna a conexão (con).
    """
    try:
        # Lê as credenciais do .env
        db_name = os.getenv("POSTGRES_NAME")
        db_user = os.getenv("POSTGRES_USER")
        db_pass = os.getenv("POSTGRES_PASSWORD")
        db_host = os.getenv("POSTGRES_HOST", "localhost")
        
        # Conecta ao banco
        con = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_pass,
            host=db_host,
            port="5432"
        )
        
        print(f"Conectado com sucesso ao banco '{db_name}' como usuário '{db_user}'.\n")
        return con
        
    except psycopg2.Error as e:
        print(f"[ERRO] Erro ao conectar ao banco de dados: {e}")
        return None
    except Exception as e:
        print(f"[ERRO] Um erro inesperado ocorreu na conexão: {e}")
        return None
