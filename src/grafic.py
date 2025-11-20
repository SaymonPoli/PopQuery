import matplotlib.pyplot as plt
import pandas as pd

# ---------------------------------------------
# Arquivo: grafic.py
# Geração automática de gráficos a partir das 3 consultas
# ---------------------------------------------

def gerar_grafico_relatorio_1(df):
    """
    Gráfico: Top 5 Bilheteria
    df deve conter colunas: ['titulo_filme', 'faturamento_total']
    """
    plt.figure()
    plt.bar(df['titulo_filme'], df['faturamento_total'])
    plt.title('Top 5 Bilheteria')
    plt.xlabel('Filme')
    plt.ylabel('Faturamento (R$)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('grafico_top5_bilheteria.png')
    plt.close()


def gerar_grafico_relatorio_2(df):
    """
    Gráfico: Faturamento por Dia da Semana
    df deve conter colunas: ['dia_da_semana', 'faturamento_total']
    """
    plt.figure()
    plt.bar(df['dia_da_semana'], df['faturamento_total'])
    plt.title('Faturamento por Dia da Semana')
    plt.xlabel('Dia da Semana')
    plt.ylabel('Faturamento (R$)')
    plt.tight_layout()
    plt.savefig('grafico_faturamento_semana.png')
    plt.close()


def gerar_grafico_relatorio_3(df):
    """
    Relação IMDb vs. Total de Ingressos Vendidos
    df deve conter colunas: ['titulo_filme', 'nota_imdb', 'total_ingressos']
    """

    plt.figure(figsize=(8, 6))

    # Cores diferentes para cada filme
    cores = plt.cm.tab20(range(len(df)))

    # Scatter plot
    plt.scatter(df['nota_imdb'], df['total_ingressos'], c=cores)

    # --- Formatação dos eixos ---
    plt.ticklabel_format(style='plain', useOffset=False)       # remove offset estranho
    plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))  # IMDb com precisão
    plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%d'))    # ingressos inteiros

    plt.title('IMDb vs. Ingressos Vendidos')
    plt.xlabel('Nota IMDb (com precisão)')
    plt.ylabel('Ingressos Vendidos (inteiro)')

    # --- Legenda com cores ---
    legend_labels = df['titulo_filme'].tolist()
    for i, label in enumerate(legend_labels):
        plt.scatter([], [], color=cores[i], label=label)

    plt.legend(title="Filmes", bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.savefig('grafico_imdb_vs_vendas.png')
    plt.close()

# Funções para receber os resultados do banco e gerar os gráficos

def processar_relatorio_1(results):
    df = pd.DataFrame(results, columns=['titulo_filme', 'faturamento_total'])
    gerar_grafico_relatorio_1(df)


def processar_relatorio_2(results):
    df = pd.DataFrame(results, columns=['dia_da_semana', 'faturamento_total'])
    gerar_grafico_relatorio_2(df)


def processar_relatorio_3(results):
    df = pd.DataFrame(results, columns=['titulo_filme', 'nota_imdb', 'total_ingressos'])
    gerar_grafico_relatorio_3(df)
