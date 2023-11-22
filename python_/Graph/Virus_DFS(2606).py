V = int(input())
E = int(input())

visited = [0] * (V+1)
graph = [[] for i in range(V+1)]

for i in range(E):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph,v,visited):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(graph,i,visited)
    return True

dfs(graph,1,visited)
print(sum(visited)-1)
