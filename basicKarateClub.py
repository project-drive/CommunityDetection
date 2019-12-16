import matplotlib.pyplot as plt
from networkx.algorithms import community
import networkx as nx

# G = nx.karate_club_graph()
G=nx.Graph()
f=open("edges.txt", "r")
for i in f:
    # print(type(i))
    x = i.split('\t')
    x[1] = x[1].replace('\n','')
    G.add_edge(x[0],x[1])


# G=nx.Graph()

communities_generator = community.girvan_newman(G)
top_level_communities = next(communities_generator)
# next_level_communities = next(communities_generator)
print(sorted(map(sorted, top_level_communities)))
