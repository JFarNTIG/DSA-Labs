import networkx as nx
import csv

def load_connection_data(data_path):
    rows = []

    with open(data_path, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            # need to transform the weight (time in hours) from string to a float
            rows.append((row[0], row[1], float(row[2])))
    
    return rows

connection_data = load_connection_data("data/connections_se.txt")

stations_graph = nx.DiGraph()
stations_graph.add_weighted_edges_from(connection_data)

station1 = "Karlstad C"
station2 = "Jönköping C"

print(f"Finding shortest path from {station1} to {station2}")

# Use Dijkstra's pathfinding algorithm to find the shortest path
# between two nodes.
path = nx.dijkstra_path(stations_graph, station1, station2)

# At this point `path` is a list of nodes along the path.
# To get edges, we will take pairs of nodes.
edges = nx.utils.pairwise(path)
for edge in edges:
    edge_weight = stations_graph.get_edge_data(edge[0], edge[1])['weight']
    print(f"{edge[0]} -> {edge[1]} ({edge_weight} hours)")

time = nx.path_weight(stations_graph, path, "weight")
print(f"Total Time: {time:.2f} hours")