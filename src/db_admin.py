# -----------------------------------------------------------------
# FUNÇÕES DE ADMIN (Item e)
# (Criar, Popular e Deletar o banco)
# -----------------------------------------------------------------

def run_sql_file(filepath, con):
    """Função genérica para ler e executar um arquivo .sql"""
    try:
        with con.cursor() as cur:
            # O caminho para a pasta sql/ é adicionado aqui
            with open(f'sql/{filepath}', 'r', encoding='utf-8') as sql_file:
                sql_script = sql_file.read()
                
            cur.execute(sql_script)
            con.commit()
        print(f"Script [ {filepath} ] executado com sucesso.")
        
    except FileNotFoundError:
        print(f"[ERRO] Arquivo não encontrado: sql/{filepath}")
    except Exception as e:
        print(f"[ERRO] Falha ao executar sql/{filepath}: {e}")
        con.rollback()

def drop_all_tables(con):
    print("\n--- [Opção 12] Deletando Todas as Tabelas ---")
    confirm = input("TEM CERTEZA? Isso apagará TODOS os dados. (s/n): ").lower()
    if confirm == 's':
        run_sql_file('drop_all_tables.sql', con)
    else:
        print("Operação cancelada.")

def create_all_tables(con):
    print("\n--- [Opção 11] Criando Todas as Tabelas ---")
    run_sql_file('create_tables.sql', con)

def populate_all_tables(con):
    print("\n--- [Opção 10] Populando Todas as Tabelas ---")
    run_sql_file('populate_cinema.sql', con)

