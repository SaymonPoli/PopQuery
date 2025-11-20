# -----------------------------------------------------------------
# RELATÓRIOS (Item c)
# Agora integrados com geração automática de gráficos
# -----------------------------------------------------------------

from src.grafic import (
    processar_relatorio_1,
    processar_relatorio_2,
    processar_relatorio_3
)

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

            results = cur.fetchall()

            print("\n--- Resultado (Tabela) ---")
            print(f"{'titulo_filme':<50} | faturamento_total")
            print("-" * 70)

            for row in results:
                print(f"{row[0]:<50} | R$ {row[1]:.2f}")

        processar_relatorio_1(results)
        print("\n[OK] Gráfico gerado: grafico_top5_bilheteria.png")

    except Exception as e:
        print(f"[ERRO] Falha ao gerar relatório: {e}")
        con.rollback()


def run_report_2(con):
    print("\n--- [Opção 7] Relatório: Vendas por Dia da Semana ---")
    try:
        query_sql = """
            SELECT
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
            GROUP BY dia_da_semana
            ORDER BY SUM(ci.valor_total) DESC;
        """

        with con.cursor() as cur:
            cur.execute(query_sql)

            results = cur.fetchall()

            print("\n--- Resultado (Tabela) ---")
            print(f"{'Dia da Semana':<20} | Faturamento")
            print("-" * 40)

            for row in results:
                print(f"{row[0]:<20} | R$ {row[1]:.2f}")

        processar_relatorio_2(results)
        print("\n[OK] Gráfico gerado: grafico_faturamento_semana.png")

    except Exception as e:
        print(f"[ERRO] Falha ao gerar relatório: {e}")
        con.rollback()


def run_report_3(con):
    print("\n--- [Opção 8] Relatório: IMDb vs Ingressos Vendidos ---")
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

            results = cur.fetchall()

            print("\n--- Resultado (Tabela) ---")
            print(f"{'Filme':<50} | {'IMDb':<5} | Ingressos")
            print("-" * 80)

            for row in results:
                print(f"{row[0]:<50} | {row[1]:<5} | {row[2]}")

        processar_relatorio_3(results)
        print("\n[OK] Gráfico gerado: grafico_imdb_vs_vendas.png")

    except Exception as e:
        print(f"[ERRO] Falha ao gerar relatório: {e}")
        con.rollback()
