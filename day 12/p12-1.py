from pprint import pprint

def traverse(graph, routes, found):
    for route in routes:
        for node in graph[route[-1]]:
            if node.isupper() and route.count(node) > 100:
                continue
            if node.islower() and route.count(node) > 0:
                continue

            visited = route.copy()
            visited.append(node)
            print(visited)
            if node == 'end':
                found.append(visited)
                continue

            traverse(graph, [visited], found)


file = open("p12-input","r")
lines = file.read().splitlines()
file.close()

edges = set()
for line in lines:
    edges.update(line.split('-'))

graph = {i : set() for i in edges}

for line in lines:
    c = line.split('-')
    graph[c[0]].add(c[1])
    graph[c[1]].add(c[0])

pprint(graph)
found = []
traverse(graph, [['start']], found)
pprint(len(found))