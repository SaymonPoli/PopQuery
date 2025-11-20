# -----------------------------------------------------------------
# PROJETO FINAL DE BANCO DE DADOS - POPQUERY (SGCINE)
# -----------------------------------------------------------------
#
# Este script é a aplicação principal (Item d) que conecta
# todos os requisitos (a, b, c, e, f).

# --- Importações Essenciais ---
from dotenv import load_dotenv 
from src.connection import connect_popquery
from src.crud import crud_menu
from src.db_admin import create_all_tables, drop_all_tables, populate_all_tables
from src.reports import run_report_1, run_report_2, run_report_3
from src.ai import run_ia_recommendation
from src.grafic import processar_relatorio_1, processar_relatorio_2, processar_relatorio_3

# Carrega as variáveis do arquivo .env para a memória
load_dotenv() 

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