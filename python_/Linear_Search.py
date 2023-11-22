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
def sSearch(n):
    total=len(ss_list)
    idx=0
    while idx<total:
        if n==ss_list[idx]:
            return idx
        idx=idx+1
    return False

totalNum=int(input("몇개의 난수를 생성할까요:"))
genRandom(totalNum)
print("리스트",len(ss_list),"개 생성")

while True:
    menu=int(input("1.선형검색 0.종료:"))
    if menu==0:
        break
    elif menu==1:
        num=int(input('찾을 숫자는:'))
        result=sSearch(num)
        if result==False:
            print("검색실패")
        else:
            print("검색성공")
            print("Index=",result)