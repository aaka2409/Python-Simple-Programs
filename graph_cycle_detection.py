# Function that detects cycle in a directed graph
def cycleCheck(vertices, adj):
    visited = set()
    ancestor = set()
    for vertex in range(vertices):
        if vertex not in visited:
            if dfs(vertex, adj, visited, ancestor)==True:
                return True
    return False
    
# Recursive dfs function
def dfs(vertex, adj, visited, ancestor):
    visited.add(vertex)
    ancestor.add(vertex)
    for neighbour in adj[vertex]:
        if neighbour not in visited:
            if dfs(neighbour, adj, visited, ancestor)==True:
                return True
        elif neighbour in ancestor:
            return True
    ancestor.remove(vertex)
    return False

print('---------------------------------------------------------------------')
print('\tCheck if a cycle exists in a directed graph')
print('---------------------------------------------------------------------\n')
t = int(input("Enter the number of testcases: "))
for _ in range(t):
    print('\n*************** Testcase', _+1, '***************\n')
    vertices, edges = map(int, input("Enter number of vertices & edges (space separated): ").split())
    # Create an adjacency list
    adj = [[] for vertex in range(vertices)]
    for edge in range(edges):
        start, end = map(int, input("Enter edge (space separated): ").split())
        adj[start].append(end)
    if cycleCheck(vertices, adj) == True:
        print('Cycle detected')
    else:
        print('No cycle detected')