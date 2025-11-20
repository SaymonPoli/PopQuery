import os
import psycopg2
import google.generativeai as genai

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
