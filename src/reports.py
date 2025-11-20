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
            GROUP BY dia_id, dia_da_semana # Agrupa pelo número e pelo nome traduzido
            ORDER BY dia_id; # Ordena pelo número (Domingo primeiro)
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
