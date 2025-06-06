import numpy as np
import pandas as pd

categorias = {
    'Alimentação': ['Supermercado', 'Padaria', 'Restaurante', 'Delivery' ],
    'Transporte': ['Uber', 'Ônibus', 'Gasolina', 'Estacionamento'],
    'Lazer': ['Streaming', 'Cinema', 'Viagem', 'Bar'],
    'Educação': ['Curso online', 'Faculdade', 'Material Didatico', 'Livros'],
    'Moradia': ['Aluguel','Condomínio','Luz','Internet','Água','Gás']
}

np.random.seed(42)
num_linhas = 500
datas = pd.date_range(start='2023-01-01', periods=num_linhas, freq='D')
dados = []

for i in range(num_linhas):
    categoria = np.random.choice(list(categorias.keys()))
    descricao = np.random.choice(categorias[categoria])
    valor = round(np.random.uniform(10, 1000), 2)
    dados.append([datas[i].date(), categoria, descricao, valor]) 

df = pd.DataFrame(dados, columns=['Data', 'Categoria', 'Descrição', 'Valor'])

df.to_csv('exemplo_gastos.csv', index=False)
print("Arquivo salvo como 'exemplo_gastos.csv'")
