import pandas as pd
import matplotlib.pyplot as plt

caminho_arquivo = '/content/exemplo_gastos.csv'
df=pd.read_csv(caminho_arquivo)

df['Data'] = pd.to_datetime(df['Data'])

totais_por_categoria = df.groupby('Categoria')['Valor'].sum().sort_values(ascending=False)

print(f'Resumo dos gastos por categoria:\n{totais_por_categoria}')

plt.figure(figsize=(12, 8))
totais_por_categoria.plot(kind='bar', color='darkblue')
plt.title('Total de gastos por categoria', size=16)
plt.xlabel('Categorias', size=13)
plt.ylabel('Valor (R$)', size=13)
plt.xticks(rotation=45, size =12, color='darkgreen')
plt.tight_layout()
plt.savefig('gastos_por_categoria.png')
plt.show()
