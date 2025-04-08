import networkx as nx
from pyvis.network import Network

# Criar o grafo com NetworkX
G = nx.Graph()
notas = ['Nota1', 'Nota2', 'Nota3', 'Nota4']

for nota in notas:
    G.add_node(nota, title=f"Conteúdo de {nota}", label=nota)

conexoes = [
    ('Nota1', 'Nota2'),
    ('Nota1', 'Nota3'),
    ('Nota2', 'Nota4'),
    ('Nota3', 'Nota4')
]

G.add_edges_from(conexoes)

# Criar visualização com PyVis
net = Network(
    height='100%', 
    width='100%', 
    bgcolor='#1e1e1e', 
    font_color='white'
)

net.from_nx(G)
net.toggle_physics(True)

# Gerar HTML no mesmo diretório (padrão)
net.show('grafico_obsidian.html')
