import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd

# ---------------------------------------------
# Arquivo: grafic.py
# Geração automática de gráficos a partir das 3 consultas
# ---------------------------------------------

plt.rcParams['font.size'] = 12        # fonte base
plt.rcParams['axes.titlesize'] = 18   # título
plt.rcParams['axes.labelsize'] = 14   # rótulos dos eixos
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 10


def gerar_grafico_relatorio_1(df):
    """
    Gráfico: Top 5 Bilheteria
    df deve conter colunas: ['titulo_filme', 'faturamento_total']
    """
    plt.figure(figsize=(10, 6))
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

    # Ordem fixa dos dias
    ordem_dias = [
        "Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira",
        "Quinta-feira", "Sexta-feira", "Sábado"
    ]

    # Reordena o df pela ordem correta
    df['dia_da_semana'] = pd.Categorical(df['dia_da_semana'], categories=ordem_dias, ordered=True)
    df = df.sort_values('dia_da_semana')

    plt.figure(figsize=(10, 6))

    plt.bar(df['dia_da_semana'], df['faturamento_total'])

    plt.title('Faturamento por Dia da Semana')
    plt.xlabel('Dia da Semana')
    plt.ylabel('Faturamento (R$)')

    plt.xticks(rotation=20, ha='right')

    plt.tight_layout()

    plt.savefig('grafico_faturamento_semana.png')
    plt.close()

def gerar_grafico_relatorio_3(df):
    plt.figure(figsize=(16, 10))  # Tamanho maior para área da legenda

    gs = gridspec.GridSpec(2, 1, height_ratios=[4, 1])  # Gráfico em cima, legenda embaixo
    ax = plt.subplot(gs[0])

    num_filmes = len(df)
    cores = plt.cm.get_cmap('nipy_spectral', num_filmes)(range(num_filmes))  # Paleta de alto contraste

    ax.scatter(df['nota_imdb'], df['total_ingressos'], c=cores)

    ax.ticklabel_format(style='plain', useOffset=False)
    ax.xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))
    ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%d'))
    ax.set_title('IMDb vs. Ingressos Vendidos')
    ax.set_xlabel('Nota IMDb')
    ax.set_ylabel('Ingressos Vendidos')

    legend_labels = df['titulo_filme'].tolist()
    handles = [plt.Line2D([], [], marker="o", color=cores[i], linestyle='', label=label) for i, label in enumerate(legend_labels)]

    ax_legenda = plt.subplot(gs[1])
    ax_legenda.axis("off")
    ax_legenda.legend(handles=handles, title="Filmes", loc="center", ncol=5, fontsize=10, title_fontsize=12)

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
