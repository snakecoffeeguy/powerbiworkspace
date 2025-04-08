import networkx as nx
from pyvis.network import Network

# Dados de exemplo (simulam tabelas do Power BI)
tabelas = ['Clientes', 'Produtos', 'Vendas', 'Pagamentos']
conexoes = [
    ('Clientes', 'Vendas'),
    ('Produtos', 'Vendas'),
    ('Vendas', 'Pagamentos')
]

# Criar grafo
G = nx.Graph()
G.add_nodes_from(tabelas)
G.add_edges_from(conexoes)

# Criar visual com PyVis
net = Network(height='750px', width='100%', bgcolor='#222222', font_color='white')
net.from_nx(G)
net.toggle_physics(True)

# Gerar o arquivo index.html para GitHub Pages
net.show('index.html')
