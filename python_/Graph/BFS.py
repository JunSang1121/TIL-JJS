import sys
from collections import deque

N,M,R = map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]

for i in range(M):
    tmp=list(map(int,sys.stdin.readline().split()))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])

for i in range(N+1):
    graph[i].sort()

def bfs(graph,R,visited):
    queue=deque([R])
    visited[R]=1
    count=2
    
    while queue:
        R=queue.popleft()
        
        for i in graph[R]:
            if visited[i]==0:
                queue.append(i)
                visited[i]=count 
                count+=1

visited=[0]*(N+1)

bfs(graph,R,visited)

for i in visited[1::]:
    print(i)