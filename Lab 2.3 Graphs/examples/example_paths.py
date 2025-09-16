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

print(f"Finding simple paths from {station1} to {station2}")

# Compute simple paths between two stations.
for path in nx.all_simple_paths(stations_graph, source=station1, target=station2, cutoff=4):
    time = nx.path_weight(stations_graph, path, "weight")
    print(" -> ".join(path))
    print(f"Total Time: {time:.2f} hours")

