N, K = map(int, input().split()) 
lst= list()
for i in range(N):
    lst.append(int(input()))

cnt = 0
for i in reversed(range(N)):
    cnt += K//lst[i]
    K = K%lst[i]

print(cnt)