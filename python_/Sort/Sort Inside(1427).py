n = int(input())
a=[]
a=list(map(int,str(n)))
a.sort(reverse=True)
for n in a:
    print(n, end="")