import random

MAX_NUM=500
MIN_NUM=1
ss_list=[]

def genRandom(n):
    c=0
    while c<n:
        num=random.randint(MIN_NUM,MAX_NUM)
        if num in ss_list:
            continue
        ss_list.append(num)
        c=c+1

totalNUM=int(input("몇개의 난수를 생성할까요:"))
genRandom(totalNUM)
print(ss_list)
print("리스트의 개수:",len(ss_list))