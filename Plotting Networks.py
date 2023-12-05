import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math

df_friendships = pd.read_csv(r"C:\Users\Pau Vila\OneDrive\RUG PhD\GUTS\Pilot Data\Directed_Friendships.csv", delimiter=',')
df_dislikes = pd.read_csv(r"C:\Users\Pau Vila\OneDrive\RUG PhD\GUTS\Pilot Data\directed_dislikes.csv", delimiter=',' )
df_support = pd.read_csv(r"C:\Users\Pau Vila\OneDrive\RUG PhD\GUTS\Pilot Data\directed_support.csv", delimiter=',' )
df_opinion = pd.read_csv(r"C:\Users\Pau Vila\OneDrive\RUG PhD\GUTS\Pilot Data\directed_opinion.csv", delimiter=',' )
df_impulsive = pd.read_csv(r"C:\Users\Pau Vila\OneDrive\RUG PhD\GUTS\Pilot Data\directed_impulsive.csv", delimiter=',' )
df_academic = pd.read_csv(r"C:\Users\Pau Vila\OneDrive\RUG PhD\GUTS\Pilot Data\directed_academic.csv", delimiter=',' )
df_helpful = pd.read_csv(r"C:\Users\Pau Vila\OneDrive\RUG PhD\GUTS\Pilot Data\directed_helpful.csv", delimiter=',' )
df_time = pd.read_csv(r"C:\Users\Pau Vila\OneDrive\RUG PhD\GUTS\Pilot Data\directed_time.csv", delimiter=',' )
df_pressure = pd.read_csv(r"C:\Users\Pau Vila\OneDrive\RUG PhD\GUTS\Pilot Data\directed_pressure.csv", delimiter=',' )


G_1 = nx.MultiDiGraph()

nodes = set(df_friendships['sender']) | set(df_friendships['receiver']) | set(df_dislikes['sender']) | set(df_dislikes['reciever'])
G_1.add_nodes_from(nodes)

friendship_edges = [(row['sender'], row['receiver'], 'friendship', {'layer': 'friendship'}) for index, row in df_friendships.iterrows()]
G_1.add_edges_from(friendship_edges)

dislike_edges = [(row['sender'], row['reciever'], 'dislike',{'layer': 'dislike'}) for index, row in df_dislikes.iterrows()]
G_1.add_edges_from(dislike_edges)

support_edges = [(row['sender'], row['reciever'], 'support',{'layer': 'support'}) for index, row in df_support.iterrows()]
G_1.add_edges_from(support_edges)

opinion_edges = [(row['sender'], row['reciever'], 'opinion',{'layer': 'opinion'}) for index, row in df_opinion.iterrows()]
G_1.add_edges_from(opinion_edges)

impulsive_edges = [(row['sender'], row['reciever'], 'impulsive',{'layer': 'impulsive'}) for index, row in df_impulsive.iterrows()]
G_1.add_edges_from(impulsive_edges)

academic_edges = [(row['sender'], row['reciever'], 'academic',{'layer': 'academic'}) for index, row in df_academic.iterrows()]
G_1.add_edges_from(academic_edges)

helpful_edges = [(row['sender'], row['reciever'], 'helpful',{'layer': 'helpful'}) for index, row in df_helpful.iterrows()]
G_1.add_edges_from(helpful_edges)

time_edges = [(row['sender'], row['reciever'], 'time',{'layer': 'time'}) for index, row in df_time.iterrows()]
G_1.add_edges_from(time_edges)

pressure_edges = [(row['sender'], row['reciever'], 'pressure',{'layer': 'presssure'}) for index, row in df_pressure.iterrows()]
G_1.add_edges_from(pressure_edges)


nan_nodes = []
for node in G_1.nodes():
    if math.isnan(node):
        nan_nodes.append(node)
G_1.remove_nodes_from(nan_nodes)

print(G_1.nodes)
nodes_with_outgoing_ties = set()
for node in G_1.nodes():
    if G_1.out_degree(node) > 0:
        nodes_with_outgoing_ties.add(node)
new_G = G_1.subgraph(nodes_with_outgoing_ties)

friendship_ties = [(u, v) for u, v, data in new_G.edges(data=True) if data['layer'] == 'friendship']
non_reciprocated_ties = []
reciprocated_ties = []
for edge in friendship_ties:
    reverse_edge = (edge[1], edge[0])
    if reverse_edge in friendship_ties:
        reciprocated_ties.append(edge)
    else:
        non_reciprocated_ties.append(edge)

time_ties = [(u, v) for u, v, data in new_G.edges(data=True) if data['layer'] == 'time']
non_reciprocated_time_ties = []
reciprocated_time_ties = []
for edge in time_ties:
    reverse_edge = (edge[1], edge[0])
    if reverse_edge in time_ties:
        reciprocated_time_ties.append(edge)
    else:
        non_reciprocated_time_ties.append(edge)

H = new_G.subgraph([128, 129, 130, 101, 103, 104, 106.0, 107.0, 109.0, 111.0, 112.0, 113.0, 115.0, 116.0, 118.0, 119.0, 120.0, 121.0, 122.0, 123.0, 124.0, 125.0, 126.0])

dislike_edges = [(u, v) for u, v, data in new_G.edges(data=True) if data['layer'] == 'dislike'] # This part of the code is probably redundant
dislike_counts = {node: sum(1 for u, v, data in new_G.edges(data=True) if v == node and data['layer'] == 'dislike') for node in new_G.nodes()}
support_counts = {node: sum(1 for u, v, data in new_G.edges(data=True) if v == node and data['layer'] == 'support') for node in new_G.nodes()}
opinion_counts = {node: sum(1 for u, v, data in new_G.edges(data=True) if v == node and data['layer'] == 'opinion') for node in new_G.nodes()}
impulsive_counts = {node: sum(1 for u, v, data in new_G.edges(data=True) if v == node and data['layer'] == 'impulsive') for node in new_G.nodes()}
academic_counts = {node: sum(1 for u, v, data in new_G.edges(data=True) if v == node and data['layer'] == 'academic') for node in new_G.nodes()}
helpful_counts = {node: sum(1 for u, v, data in new_G.edges(data=True) if v == node and data['layer'] == 'helpful') for node in new_G.nodes()}
time_counts = {node: sum(1 for u, v, data in new_G.edges(data=True) if v == node and data['layer'] == 'time') for node in new_G.nodes()}
pressure_counts = {node: sum(1 for u, v, data in new_G.edges(data=True) if v == node and data['layer'] == 'pressure') for node in new_G.nodes()}

pos = nx.spring_layout(new_G, 0.5/math.sqrt(len(H.nodes)), weight=0.5)
#pos = nx.kamada_kawai_layout(new_G, scale=400)


########### Dislike plot ############

plt.figure(figsize=(12, 10))
nx.draw_networkx_edges(new_G, pos, edgelist=non_reciprocated_ties, edge_color='white', width=0.5, connectionstyle="arc3,rad=0.1", arrowstyle="-")
nx.draw_networkx_edges(new_G, pos, edgelist=reciprocated_ties, edge_color='black', width=3.0, connectionstyle="arc3,rad=0.1", arrowstyle="-")
nx.draw_networkx_edges(new_G, pos, edgelist=dislike_edges, edge_color='darkred', width=0.5, connectionstyle="arc3,rad=0.1")
minimum_node_size = 6
for node, size in dislike_counts.items():
    if size > 0:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=size * 6, node_color='black')
    else:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=minimum_node_size, node_color='black')
friendship_legend = mpatches.Patch(color='black', label='Friendship')
dislike_legend = mpatches.Patch(color='darkred', label='Dislike')
legend = plt.legend(handles=[friendship_legend, dislike_legend], loc='upper right')
frame = legend.get_frame()
frame.set_facecolor('lightgray')
plt.axis('off')
plt.savefig('dislike.png')
plt.show()

########### Support plot ############

plt.figure(figsize=(12, 10))
nx.draw_networkx_edges(new_G, pos, edgelist=non_reciprocated_ties, edge_color='white', width=0.5, connectionstyle="arc3,rad=0.1", arrowstyle="-")
nx.draw_networkx_edges(new_G, pos, edgelist=reciprocated_ties, edge_color='black', width=3.0, connectionstyle="arc3,rad=0.1", arrowstyle="-")
nx.draw_networkx_edges(new_G, pos, edgelist=support_edges, edge_color='g', width=0.5, connectionstyle="arc3,rad=0.1")
minimum_node_size = 10
for node, size in support_counts.items():
    if size > 0:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=size * 15, node_color='black')
    else:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=minimum_node_size, node_color='black')
friendship_legend = mpatches.Patch(color='black', label='Friendship')
dislike_legend = mpatches.Patch(color='g', label='Support')
legend = plt.legend(handles=[friendship_legend, dislike_legend], loc='upper right')
frame = legend.get_frame()
frame.set_facecolor('lightgray')
plt.axis('off')
plt.savefig('support.png')
plt.show()

########### Opinion plot ############

plt.figure(figsize=(12, 10))
nx.draw_networkx_edges(new_G, pos, edgelist=non_reciprocated_ties, edge_color='white', width=0.5, connectionstyle="arc3,rad=0.1")
nx.draw_networkx_edges(new_G, pos, edgelist=reciprocated_ties, edge_color='black', width=3.0, connectionstyle="arc3,rad=0.1", arrowstyle="-")
nx.draw_networkx_edges(new_G, pos, edgelist=opinion_edges, edge_color='darkorange', width=0.5, connectionstyle="arc3,rad=0.1")
minimum_node_size = 10
for node, size in opinion_counts.items():
    if size > 0:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=size * 15, node_color='black')
    else:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=minimum_node_size, node_color='black')
friendship_legend = mpatches.Patch(color='black', label='Friendship')
dislike_legend = mpatches.Patch(color='darkorange', label='Opinion')
legend = plt.legend(handles=[friendship_legend, dislike_legend], loc='upper right')
frame = legend.get_frame()
frame.set_facecolor('lightgray')
plt.axis('off')
plt.show()

########### Impulsive plot ############

plt.figure(figsize=(12, 10))
nx.draw_networkx_edges(new_G, pos, edgelist=non_reciprocated_ties, edge_color='white', width=0.5, connectionstyle="arc3,rad=0.1")
nx.draw_networkx_edges(new_G, pos, edgelist=reciprocated_ties, edge_color='black', width=3.0, connectionstyle="arc3,rad=0.1", arrowstyle="-")
nx.draw_networkx_edges(new_G, pos, edgelist=impulsive_edges, edge_color='crimson', width=0.5, connectionstyle="arc3,rad=0.1")
minimum_node_size = 10
for node, size in impulsive_counts.items():
    if size > 0:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=size * 15, node_color='black')
    else:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=minimum_node_size, node_color='black')
friendship_legend = mpatches.Patch(color='black', label='Friendship')
dislike_legend = mpatches.Patch(color='crimson', label='Impulsive')
legend = plt.legend(handles=[friendship_legend, dislike_legend], loc='upper right')
frame = legend.get_frame()
frame.set_facecolor('lightgray')
plt.axis('off')
plt.show()

########### Academic plot ############

plt.figure(figsize=(12, 10))
nx.draw_networkx_edges(new_G, pos, edgelist=non_reciprocated_ties, edge_color='white', width=0.5, connectionstyle="arc3,rad=0.1")
nx.draw_networkx_edges(new_G, pos, edgelist=reciprocated_ties, edge_color='black', width=3.0, connectionstyle="arc3,rad=0.1", arrowstyle="-")
nx.draw_networkx_edges(new_G, pos, edgelist=academic_edges, edge_color='goldenrod', width=0.5, connectionstyle="arc3,rad=0.1")
minimum_node_size = 10
for node, size in academic_counts.items():
    if size > 0:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=size * 15, node_color='black')
    else:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=minimum_node_size, node_color='black')
friendship_legend = mpatches.Patch(color='black', label='Friendship')
dislike_legend = mpatches.Patch(color='goldenrod', label='Academic')
legend = plt.legend(handles=[friendship_legend, dislike_legend], loc='upper right')
frame = legend.get_frame()
frame.set_facecolor('lightgray')
plt.axis('off')
plt.show()

########### Helpful plot ############

plt.figure(figsize=(12, 10))
nx.draw_networkx_edges(new_G, pos, edgelist=non_reciprocated_ties, edge_color='white', width=0.5, connectionstyle="arc3,rad=0.1")
nx.draw_networkx_edges(new_G, pos, edgelist=reciprocated_ties, edge_color='black', width=3.0, connectionstyle="arc3,rad=0.1", arrowstyle="-")
nx.draw_networkx_edges(new_G, pos, edgelist=helpful_edges, edge_color='saddlebrown', width=0.5, connectionstyle="arc3,rad=0.1")
minimum_node_size = 10
for node, size in helpful_counts.items():
    if size > 0:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=size * 15, node_color='black')
    else:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=minimum_node_size, node_color='black')
friendship_legend = mpatches.Patch(color='black', label='Friendship')
dislike_legend = mpatches.Patch(color='saddlebrown', label='Helpful')
legend = plt.legend(handles=[friendship_legend, dislike_legend], loc='upper right')
frame = legend.get_frame()
frame.set_facecolor('lightgray')
plt.axis('off')
plt.show()


########### Pressure plot ############

plt.figure(figsize=(12, 10))
nx.draw_networkx_edges(new_G, pos, edgelist=non_reciprocated_ties, edge_color='white', width=0.5, connectionstyle="arc3,rad=0.1")
nx.draw_networkx_edges(new_G, pos, edgelist=reciprocated_ties, edge_color='black', width=3.0, connectionstyle="arc3,rad=0.1", arrowstyle="-")
nx.draw_networkx_edges(new_G, pos, edgelist=pressure_edges, edge_color='firebrick', width=0.5, connectionstyle="arc3,rad=0.1")
minimum_node_size = 10
for node, size in pressure_counts.items():
    if size > 0:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=size * 15, node_color='black')
    else:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=minimum_node_size, node_color='black')
friendship_legend = mpatches.Patch(color='black', label='Friendship')
dislike_legend = mpatches.Patch(color='firebrick', label='Pressure')
legend = plt.legend(handles=[friendship_legend, dislike_legend], loc='upper right')
frame = legend.get_frame()
frame.set_facecolor('lightgray')
plt.axis('off')
plt.show()


########## Time Plot for Overlap ##########

plt.figure(figsize=(12, 10))
nx.draw_networkx_edges(new_G, pos, edgelist=non_reciprocated_time_ties, edge_color='black', width=0.5, connectionstyle="arc3,rad=0.1")
nx.draw_networkx_edges(new_G, pos, edgelist=reciprocated_time_ties, edge_color='black', width=3.0, connectionstyle="arc3,rad=0.1", arrowstyle="-")
#nx.draw_networkx_edges(new_G, pos, edgelist=time_edges, edge_color='black', width=1, connectionstyle="arc3,rad=0.1")
minimum_node_size = 10
for node, size in pressure_counts.items():
    if size > 0:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=100, node_color='black')
    else:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=100, node_color='black')
#nx.draw_networkx_nodes(H, poc, nodelist=[node], node_size=200, node_color='black')
time_legend = mpatches.Patch(color='black', label='Prefer to spend time with')
legend = plt.legend(handles=[time_legend], loc='upper right')
frame = legend.get_frame()
frame.set_facecolor('lightgray')
plt.axis('off')
plt.show()


########## Friendship Plot for Overlap ##########

plt.figure(figsize=(12, 10))
nx.draw_networkx_edges(new_G, pos, edgelist=non_reciprocated_ties, edge_color='black', width=0.5, connectionstyle="arc3,rad=0.1")
nx.draw_networkx_edges(new_G, pos, edgelist=reciprocated_ties, edge_color='black', width=3.0, connectionstyle="arc3,rad=0.1", arrowstyle="-")
#nx.draw_networkx_edges(new_G, pos, edgelist=time_edges, edge_color='black', width=1, connectionstyle="arc3,rad=0.1")
minimum_node_size = 10
for node, size in pressure_counts.items():
    if size > 0:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=100, node_color='black')
    else:
        nx.draw_networkx_nodes(H, pos, nodelist=[node], node_size=100, node_color='black')
#nx.draw_networkx_nodes(H, poc, nodelist=[node], node_size=200, node_color='black')
friendship_legend = mpatches.Patch(color='black', label='Friendship')
legend = plt.legend(handles=[friendship_legend], loc='upper right')
frame = legend.get_frame()
frame.set_facecolor('lightgray')
plt.axis('off')
plt.show()



