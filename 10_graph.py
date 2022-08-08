'''Graph'''

class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("Graph Dict:", self.graph_dict)

    def getPath(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.getPath(node, end, path)
                for p in new_path:
                    paths.append(p)

        return paths


    def shortestPath(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]
        
        if start not in self.graph_dict:
            return None

        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.shortestPath(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

        '''Alternate Method of finding the Shortest Path'''

        # def shortestPath(self, start, end):
        # s_path = self.getPath(start, end)

        # shortest_path = None
        # for p in s_path:
        #     if shortest_path is None or len(p) < len(shortest_path):
        #         shortest_path = p

        # return shortest_path

        

if __name__ == '__main__':
    routes = [
        ("Peshawar", "London"),
        ("Peshawar", "Dubai"),
        ("London", "Dubai"),
        ("London", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    route_graph = Graph(routes)

    start = "Peshawar"
    end = "New York"

    print(f"Paths Between {start} and {end}:", route_graph.getPath(start, end)) 
    print(f"Shortest path Between {start} and {end}:", route_graph.shortestPath(start, end)) 