import networkx as nx
from pyvis.network import Network
import os

# Dados fictícios (poderiam vir de um CSV exportado do Power BI, por exemplo)
tabelas = ['Clientes', 'Produtos', 'Vendas', 'Pagamentos']
conexoes = [('Clientes', 'Vendas'), ('Produtos', 'Vendas'), ('Vendas', 'Pagamentos')]

# Gera o grafo
G = nx.Graph()
G.add_nodes_from(tabelas)
G.add_edges_from(conexoes)

net = Network(height='750px', width='100%', bgcolor='#222222', font_color='white')
net.from_nx(G)
net.show('index.html')

# Git automation (opcional)
os.system('git add index.html')
os.system('git commit -m "Atualização automática do grafo"')
os.system('git push')
