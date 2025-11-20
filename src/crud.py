from psycopg2 import errors

# -----------------------------------------------------------------
# FUNÇÕES CRUD (Item b)
# Inspirado no 'update_value' e 'show_table' do professor
# -----------------------------------------------------------------

def inserir_registro(con):
    """ (Create) Insere um novo registro em uma tabela. """
    print("\n--- Inserir Novo Registro (Create) ---")
    try:
        table_name = input("Nome da tabela (ex: Filme): ")
        
    
        with con.cursor() as cur:
            cur.execute(f"SELECT * FROM {table_name} LIMIT 0;")
            col_names = [desc[0] for desc in cur.description if not desc[0].startswith('id_')]
        
        print(f"Colunas disponíveis: {', '.join(col_names)}")
        
        col_input = input("Digite as colunas que você quer preencher (separadas por vírgula): ").split(',')
        val_input = input(f"Digite os valores para ({', '.join(col_input)}) (separadas por vírgula): ").split(',')
        
       
        cols = [col.strip() for col in col_input]
        vals = [val.strip() for val in val_input]
        
        
        query = f"INSERT INTO {table_name} ({', '.join(cols)}) VALUES ({', '.join(['%s'] * len(vals))})"
        
        with con.cursor() as cur:
            cur.execute(query, vals)
            con.commit()
        
        print(f"Registro inserido com sucesso em {table_name}!")
        
    except Exception as e:
        print(f"[ERRO] Falha ao inserir registro: {e}")
        con.rollback()

def consultar_tabela(con):
    """ (Read) Mostra todos os dados de uma tabela. """
    print("\n--- [Opção 1] Consultar Tabela (Read) ---")
    try:
        table_name = input("Digite o nome da tabela que deseja consultar (ex: Filme): ")
        
        with con.cursor() as cur:
            cur.execute(f"SELECT * FROM {table_name};")
            
          
            col_names = [desc[0] for desc in cur.description]
            print("\n--- Resultado para:", table_name, "---")
            print(col_names) 
            
            
            for row in cur.fetchall():
                print(row)
            
    except Exception as e:
        print(f"[ERRO] Falha ao consultar tabela: {e}")
        con.rollback()

def atualizar_registro(con):
    """ (Update) Atualiza uma coluna de um registro. """
    print("\n--- Atualizar Registro (Update) ---")
    try:
        table_name = input("Nome da tabela (ex: Filme): ")
        col_update = input("Nome da coluna para ATUALIZAR (ex: nota_imdb): ")
        new_value = input(f"Digite o NOVO valor para {col_update}: ")
        col_pk = input("Nome da coluna de ID (ex: id_filme): ")
        id_value = input(f"Digite o ID do registro que você quer mudar: ")
        
       
        query = f"UPDATE {table_name} SET {col_update} = %s WHERE {col_pk} = %s"
        
        with con.cursor() as cur:
            cur.execute(query, (new_value, id_value))
            con.commit()
        
        print(f"Registro {id_value} atualizado com sucesso em {table_name}!")

    except Exception as e:
        print(f"[ERRO] Falha ao atualizar registro: {e}")
        con.rollback()

def deletar_registro(con):
    """ (Delete) Deleta um registro pelo ID. """
    print("\n--- Deletar Registro (Delete) ---")
    try:
        table_name = input("Nome da tabela (ex: Filme): ")
        col_pk = input("Nome da coluna de ID (ex: id_filme): ")
        id_value = input(f"Digite o ID do registro que você quer DELETAR: ")
        
        confirm = input(f"TEM CERTEZA que quer deletar o registro {id_value} da tabela {table_name}? (s/n): ").lower()
        
        if confirm == 's':
            query = f"DELETE FROM {table_name} WHERE {col_pk} = %s"
            
            with con.cursor() as cur:
                cur.execute(query, (id_value,))
                con.commit()
            print("Registro deletado com sucesso!")
        else:
            print("Operação cancelada.")
            
    except errors.ForeignKeyViolation as e:
        print(f"\n[ERRO DE DEPENDÊNCIA] Não foi possível deletar o registro.")
        print("Ele está sendo usado por outra tabela (ex: um Filme não pode ser deletado se tiver uma Sessao).")
        print("DELETE foi cancelado (rollback).")
        con.rollback()
    except Exception as e:
        print(f"[ERRO] Falha ao deletar registro: {e}")
        con.rollback()

def crud_menu(con):
    """ Sub-menu para as operações de CRUD. """
    while True:
        crud_interface = """
    --- Menu CRUD (Item b) ---
    [1] Inserir Registro (Create)
    [2] Consultar Tabela (Read)
    [3] Atualizar Registro (Update)
    [4] Deletar Registro (Delete)
    [0] Voltar ao Menu Principal
    
    Escolha uma opção: """
        choice = input(crud_interface)
        
        if choice == '0':
            break
        elif choice == '1':
            inserir_registro(con)
        elif choice == '2':
            consultar_tabela(con)
        elif choice == '3':
            atualizar_registro(con)
        elif choice == '4':
            deletar_registro(con)
        else:
            print("\n[ERRO] Opção inválida! Tente novamente.")
