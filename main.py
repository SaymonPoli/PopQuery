# -----------------------------------------------------------------
# PROJETO FINAL DE BANCO DE DADOS - POPQUERY (SGCINE)
# -----------------------------------------------------------------
#
# Este script é a aplicação principal (Item d) que conecta
# todos os requisitos (a, b, c, e, f).

# --- Importações Essenciais ---
import psycopg2 
from psycopg2 import errors 
import os 
from dotenv import load_dotenv 
import google.generativeai as genai 


# Carrega as variáveis do arquivo .env para a memória
load_dotenv() 

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
        db_name = os.getenv("DATABASE")
        db_user = os.getenv("USER")
        db_pass = os.getenv("PASSWORD")
        db_host = os.getenv("HOST")
        
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

# -----------------------------------------------------------------
# FUNÇÕES DE ADMIN (Item e)
# (Criar, Popular e Deletar o banco)
# -----------------------------------------------------------------

def run_sql_file(filepath, con):
    """Função genérica para ler e executar um arquivo .sql"""
    try:
        with con.cursor() as cur:
            with open(filepath, 'r', encoding='utf-8') as sql_file:
                sql_script = sql_file.read()
                
            cur.execute(sql_script)
            con.commit()
        print(f"Script [ {filepath} ] executado com sucesso.")
        
    except FileNotFoundError:
        print(f"[ERRO] Arquivo não encontrado: {filepath}")
    except Exception as e:
        print(f"[ERRO] Falha ao executar {filepath}: {e}")
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
        val_input = input(f"Digite os valores para ({', '.join(col_input)}) (separados por vírgula): ").split(',')
        
       
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

# -----------------------------------------------------------------
# FUNÇÕES DE RELATÓRIO (Item c)
# (As 3 consultas de sumarização - SEM GRÁFICOS)
# -----------------------------------------------------------------

def run_report_1(con):
    print("\n--- [Opção 6] Relatório: Top 5 Bilheteria ---")
    try:
        query_sql = """
            SELECT
                f.nome AS titulo_filme,
                SUM(ci.valor_total) AS faturamento_total
            FROM Filme f
            JOIN Sessao s ON f.id_filme = s.fk_id_filme
            JOIN Ingresso i ON s.id_sessao = i.fk_id_sessao
            JOIN Cliente_Ingresso ci ON i.id_ingresso = ci.fk_id_ingresso
            GROUP BY f.nome
            ORDER BY faturamento_total DESC
            LIMIT 5;
        """
        with con.cursor() as cur:
            cur.execute(query_sql)
            

            col_names = [desc[0] for desc in cur.description]
            print("\n--- Resultado (Tabela) ---")
            print(f"{col_names[0]:<50} | {col_names[1]}") # Formata o cabeçalho
            print("-" * 70)
            
            
            results = cur.fetchall()
            for row in results:
                print(f"{str(row[0]):<50} | R$ {row[1]:.2f}")
        
        print("\n[AVISO] Para o Item (c), copie a tabela acima e cole no Excel para gerar o gráfico.")

    except Exception as e:
        print(f"[ERRO] Falha ao gerar relatório: {e}")
        con.rollback()


def run_report_2(con):
    print("\n--- [Opção 7] Relatório: Vendas por Dia da Semana ---")
    try:
       
        query_sql = """
            SELECT
                EXTRACT(DOW FROM ci.data_emissao) AS dia_id,
                
                CASE EXTRACT(DOW FROM ci.data_emissao)
                    WHEN 0 THEN 'Domingo'
                    WHEN 1 THEN 'Segunda-feira'
                    WHEN 2 THEN 'Terça-feira'
                    WHEN 3 THEN 'Quarta-feira'
                    WHEN 4 THEN 'Quinta-feira'
                    WHEN 5 THEN 'Sexta-feira'
                    WHEN 6 THEN 'Sábado'
                END AS dia_da_semana,
                
                SUM(ci.valor_total) AS faturamento_total
            FROM Cliente_Ingresso ci
            JOIN Ingresso i ON ci.fk_id_ingresso = i.id_ingresso
            JOIN Sessao s ON i.fk_id_sessao = s.id_sessao 
            GROUP BY dia_id, dia_da_semana -- Agrupa pelo número e pelo nome traduzido
            ORDER BY dia_id; -- Ordena pelo número (Domingo primeiro)
        """
       
        
        with con.cursor() as cur:
            cur.execute(query_sql)
            
           
            col_names = [desc[0] for desc in cur.description[1:]] 
            print("\n--- Resultado (Tabela) ---")
            print(f"{col_names[0]:<20} | {col_names[1]}")
            print("-" * 40)
            
            
            results = cur.fetchall()
            for row in results:
              
                print(f"{str(row[1]):<20} | R$ {row[2]:.2f}")
        
        print("\n[AVISO] Para o Item (c), copie a tabela acima e cole no Excel para gerar o gráfico.")

    except Exception as e:
        print(f"[ERRO] Falha ao gerar relatório: {e}")
        con.rollback()

def run_report_3(con):
    print("\n--- [Opção 8] Relatório: Relação IMDb vs. Vendas ---")
    try:
        query_sql = """
            SELECT
                f.nome AS titulo_filme,
                f.nota_imdb,
                SUM(ci.quantidade) AS total_ingressos_vendidos
            FROM Filme f
            JOIN Sessao s ON f.id_filme = s.fk_id_filme
            JOIN Ingresso i ON s.id_sessao = i.fk_id_sessao
            JOIN Cliente_Ingresso ci ON i.id_ingresso = ci.fk_id_ingresso
            GROUP BY f.id_filme, f.nome, f.nota_imdb
            ORDER BY total_ingressos_vendidos DESC;
        """
        with con.cursor() as cur:
            cur.execute(query_sql)
            
            col_names = [desc[0] for desc in cur.description]
            print("\n--- Resultado (Tabela) ---")
            print(f"{col_names[0]:<50} | {col_names[1]:<10} | {col_names[2]}")
            print("-" * 80)
            
            results = cur.fetchall()
            for row in results:
                print(f"{str(row[0]):<50} | {str(row[1]):<10} | {row[2]}")
        
        print("\n[AVISO] Para o Item (c), copie a tabela acima e cole no Excel para gerar o gráfico.")

    except Exception as e:
        print(f"[ERRO] Falha ao gerar relatório: {e}")
        con.rollback()

# -----------------------------------------------------------------
# FUNÇÃO DE IA (Item f)
# (Recomendação personalizada)
# -----------------------------------------------------------------
def run_ia_recommendation(con):
    """
    Busca dados do cliente no BD, envia para o LLM e imprime uma recomendação.
    """
    print("\n--- [Opção 9] Recomendação Personalizada (IA) ---")
    try:
        id_cliente = int(input("Para qual ID de cliente você quer a recomendação?: "))
        
        with con.cursor() as cur:
           
            
            # Query A: Buscar o nome do cliente
            cur.execute("SELECT nome FROM Cliente WHERE id_cliente = %s", (id_cliente,))
            nome_cliente_result = cur.fetchone()
            if not nome_cliente_result:
                print(f"[ERRO] Cliente com ID {id_cliente} não encontrado.")
                return
            nome_cliente = nome_cliente_result[0]

            # Query B: Buscar os 3 gêneros favoritos do cliente (baseado no histórico)
            query_gostos = """
                SELECT g.descricao, COUNT(g.id_genero) as contagem
                FROM Genero g
                JOIN Filme f ON g.id_genero = f.fk_id_genero
                JOIN Sessao s ON f.id_filme = s.fk_id_filme
                JOIN Ingresso i ON s.id_sessao = i.fk_id_sessao
                JOIN Cliente_Ingresso ci ON i.id_ingresso = ci.fk_id_ingresso
                WHERE ci.fk_id_cliente = %s
                GROUP BY g.descricao
                ORDER BY contagem DESC
                LIMIT 3;
            """
            cur.execute(query_gostos, (id_cliente,))
            gostos_raw = cur.fetchall()
            
            if not gostos_raw:
                print(f"O cliente {nome_cliente} (ID {id_cliente}) não tem histórico de compras.")
                return

            gostos_formatados = ", ".join([gosto[0] for gosto in gostos_raw])

            # Query C: Buscar os filmes atualmente em cartaz
            query_cartaz = """
                SELECT DISTINCT f.nome, g.descricao
                FROM Filme f
                JOIN Sessao s ON f.id_filme = s.fk_id_filme
                JOIN Genero g ON f.fk_id_genero = g.id_genero
                WHERE s.data >= CURRENT_DATE;
            """
            cur.execute(query_cartaz)
            filmes_raw = cur.fetchall()
            filmes_formatados = ", ".join([f"{filme[0]} ({filme[1]})" for filme in filmes_raw])
            
        print(f"\nOk, {nome_cliente}! Analisando seus gêneros favoritos: [{gostos_formatados}]")
        print("Buscando recomendações nos filmes em cartaz...")

        # --- PARTE 2: CHAMAR A IA GENERATIVA (LLM) ---
        
        GEMINI_API_KEY = os.getenv("GEMINI_KEY")
        if not GEMINI_API_KEY:
            print("[ERRO DE CONFIGURAÇÃO] Chave 'GEMINI_KEY' não encontrada no arquivo .env")
            return
            
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')

        prompt_para_ia = f"""
        Você é o "PopQuery", um assistente de cinema amigável.
        O cliente {nome_cliente} pediu uma recomendação.
        - Gêneros favoritos dele(a): {gostos_formatados}.
        - Filmes em cartaz: {filmes_formatados}.
        
        Tarefa: Escreva uma saudação e uma recomendação de 1 ou 2 filmes em cartaz 
        que se encaixem perfeitamente nos gêneros favoritos do cliente.
        Justifique o porquê da recomendação.
        """

        response = model.generate_content(prompt_para_ia)
        
        # --- PARTE 3: EXIBIR O RESULTADO ---
        print("\n--- Recomendação Pronta! ---")
        print(response.text)
        print("------------------------------\n")
        
    except (Exception, psycopg2.Error) as e:
        print(f"\n[ERRO] Não foi possível gerar a recomendação: {e}")
        con.rollback()

# -----------------------------------------------------------------
# PROGRAMA PRINCIPAL (MAIN) (Item d)
# (O Menu de Opções)
# -----------------------------------------------------------------

def main():
    """
    Função principal que executa o menu de opções.
    """
    con = connect_popquery()
    if not con:
        print("Encerrando o programa. Verifique suas credenciais no .env ou o status do servidor PostgreSQL.")
        return

    while True:
        interface = """
      --- MENU PRINCIPAL POPQUERY (SGCINE) ---
      
      --- Operações CRUD (Item b) ---
      [1] Gerenciar Tabelas (Inserir, Consultar, Atualizar, Deletar)
      
      --- Relatórios (Item c) ---
      [6] Relatório: Top 5 Bilheteria (tabular)
      [7] Relatório: Vendas por Dia da Semana (tabular)
      [8] Relatório: Relação IMDb vs. Vendas (tabular)
      
      --- IA (Item f) ---
      [9] Receber Recomendação de Filme (IA)
      
      --- Administração do Banco (Item e) ---
      [10] Popular Banco (Rodar DML - inserts)
      [11] Criar Tabelas (Rodar DDL - creates)
      [12] DELETAR TUDO (Rodar DROP)
      
      [0] Sair do Programa
      
      Escolha uma opção: """
        
        choice = input(interface)
        
        if choice == '0':
            print("Desconectando do banco de dados...")
            if con:
                con.close()
            print("Desconectado. Até logo!")
            break
            
        # Opções de Admin (Item e)
        elif choice == '12':
            drop_all_tables(con)
        elif choice == '11':
            create_all_tables(con)
        elif choice == '10':
            populate_all_tables(con)

        # Opções de CRUD (Item b)
        elif choice == '1':
            crud_menu(con)
        
        # Opções de Relatório (Item c)
        elif choice == '6':
            run_report_1(con)
        elif choice == '7':
            run_report_2(con)
        elif choice == '8':
            run_report_3(con)
        
        # Opção de IA (Item f)
        elif choice == '9':
            run_ia_recommendation(con)

        else:
            print("\n[ERRO] Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
