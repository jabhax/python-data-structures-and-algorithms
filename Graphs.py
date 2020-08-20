''' Graphs '''
import json


# Graph-Node Implementation with weight, direction
class GraphNode:
    def __init__(self, v, w=0, d=None):
        self.value = v
        self.weight = w
        self.direction = d


# Undirected & Unweighted Graph Implementation (weight=0, direction=None)
class UndirectedUnweightedGraph:
    # Constructor
    def __init__(self):
        self.num_nodes = 0
        self.num_edges = 0
        self.adjac_list = {}

    # Add a Vertex Implementation
    def add_vertex(self, n):
        self.adjac_list[n.value] = []
        self.num_nodes += 1

    # Add an Edge Implementation
    def add_edge(self, n1, n2):
        if self.num_nodes < 2:
            print(f'Cannot add edges. Requires 2 nodes to add an edge and '
                  f'Graph has {self.num_nodes} nodes')
        if not(n1 in self.adjac_list[n2]) and not(n2 in self.adjac_list[n1]):
            self.adjac_list[n1].append(n2)
            self.adjac_list[n2].append(n1)
            self.num_edges += 1
        else:
            print(f'Edge already exists for ({n1}, {n2}):\n. {n1}--> '
                  f'{self.adjac_list[n1]}\n. {n2}-->{self.adjac_list[n2]}')

    # Show Connections Implementation
    def show_connections(self):
        for node_value in self.adjac_list:
            print(f'{node_value}-->{self.adjac_list[node_value]}')


def main():
    # Example Graph Representations
    # Edge-List Graph
    edge_list_graph = [[0, 2], [2, 3], [2, 1], [1, 3]]
    # Adjacency-List Graph using Dictionary
    adjacency_list_graph_1 = {
      0: [2],
      1: [2, 3],
      2: [0, 1, 3],
      3: [1, 2]
    }
    # Adjacency-List Graph using Array
    adjacency_list_graph_2 = [[2], [2, 3], [0, 1, 3], [1, 2]]
    # Adjacency-Matrix Graph using 2-D Arrays
    adjacent_matrix = [
        [0, 0, 1, 0],  # index 0 is connected to node at index 2
        [0, 0, 1, 1],  # index 1 is connected to nodes at index 2 and 3
        [1, 1, 0, 1],  # index 2 is connected to nodes at index 0, 1, and 3
        [0, 1, 1, 0]   # index 3 is connected to nodes at index 1 and 2
    ]
    print(f'Edge List: {edge_list_graph}\n')
    print(f'Adjacency List 1: '
          f'{json.dumps(adjacency_list_graph_1, indent=4)}\n')
    print(f'Adjacency List 2: '
          f'{json.dumps(adjacency_list_graph_2, indent=4)}\n')
    print(f'Adjacent Matrix: '
          f'{json.dumps(adjacent_matrix, indent=4)}\n')

    # Test Graph Implementations
    graph = UndirectedUnweightedGraph()
    for i in range(6):
        # Test adding of vertex
        graph.add_vertex(GraphNode(i))
    # Test adding of edges
    graph.add_edge(1, 3)
    graph.add_edge(1, 2)
    graph.add_edge(0, 5)
    graph.add_edge(5, 4)
    graph.add_edge(5, 1)
    # Test showing graph connections after adding vertices & edges.
    graph.show_connections()
    graph.add_edge(5, 1)


if __name__ == '__main__':
    main()
