# Carregando biblioteca
import pandas as pd
import matplotlib.pyplot as plt

# Supondo que o DataFrame já esteja carregado com as informações de vendas
df = pd.DataFrame(...)

# Convertando coluna data para datetime
df['Data'] = pd.to_datetime(df['Data'])

# Criar uma nova coluna no DataFrame com o mês correspondente
df['Mes'] = df['Data'].dt.month

# Calcular o valor total de vendas por mês:
vendas_por_mes = df.groupby('Mes')['Valor'].sum()

# Criar o gráfico de barras
vendas_por_mes.plot(kind='bar')
plt.xlabel('Mês')
plt.ylabel('Valor Total de Vendas')
plt.title('Valor Total de Vendas por Mês')
plt.show()
