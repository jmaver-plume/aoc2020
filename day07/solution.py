import re


def parse():
    with open('input') as f:
        data = f.read()
    raw_lines = data.split('\n')
    parsed_lines = []
    for raw_line in raw_lines:
        bag, raw_contents = re.match(r"(.*) bags? contain (.*)\.", raw_line).groups()
        raw_contents = raw_contents.split(',')
        contents = []
        for raw_content in raw_contents:
            if raw_content == 'no other bags':
                break
            count, name = re.match(r"(\d+) (.*) bags?", raw_content.strip()).groups()
            contents.append((name, count))
        parsed_lines.append((bag, contents))
    return parsed_lines


class Edge:
    def __init__(self, source, end, weight=None):
        self.source = source
        self.end = end
        self.weight = weight


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, node):
        self.nodes.add(node)
        self.edges[node] = []

    def add_edge(self, edge):
        self.edges[edge.source].append(edge)

    def get_edges(self, node):
        return self.edges[node]

    def reverse(self):
        graph = Graph()
        for node in self.nodes:
            graph.add_node(node)

        for source in self.edges:
            for edge in self.edges[source]:
                graph.add_edge(Edge(edge.end, source, edge.weight))
        return graph


def p1():
    lines = parse()
    graph = Graph()
    for line in lines:
        graph.add_node(line[0])
        for end in line[1]:
            graph.add_edge(Edge(line[0], end[0], int(end[1])))

    reversed_graph = graph.reverse()

    visited = set()
    stack = ['shiny gold']
    while len(stack) != 0:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        edges = reversed_graph.get_edges(node)
        for edge in edges:
            stack.append(edge.end)

    visited.discard('shiny gold')
    return len(visited)


def p2():
    lines = parse()

    graph = Graph()
    for line in lines:
        graph.add_node(line[0])
        for end in line[1]:
            graph.add_edge(Edge(line[0], end[0], int(end[1])))

    cache = {}

    def get_size(node):
        sizes = []
        for edge in graph.get_edges(node):
            if edge in cache:
                sizes.append(edge.weight * cache[edge])
            else:
                sizes.append(edge.weight * get_size(edge.end))
        return 1 + sum(sizes)

    return get_size('shiny gold') - 1


def main():
    print(f'p1: {p1()}')
    print(f'p2: {p2()}')


main()
