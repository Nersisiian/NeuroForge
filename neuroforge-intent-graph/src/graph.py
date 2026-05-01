import networkx as nx
import json

class IntentGraph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_intent(self, id, action, params):
        self.graph.add_node(id, action=action, params=params)

    def to_dict(self):
        return nx.node_link_data(self.graph)

if __name__ == '__main__':
    g = IntentGraph()
    g.add_intent("001", "open_file", {"path": "/secret"})
    print(json.dumps(g.to_dict(), indent=2))
