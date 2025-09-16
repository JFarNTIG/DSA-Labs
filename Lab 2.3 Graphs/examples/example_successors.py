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


## YOUR CODE STARTS HERE




## YOUR CODE ENDS HERE