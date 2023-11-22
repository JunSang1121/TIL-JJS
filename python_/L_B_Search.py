import random
import time

MAX_NUM = 60000
MIN_NUM = 1
ss_list = []  # 선형탐색 리스트
bb_list = []  # 이진탐색 리스트

cnt = 0


def genRandom(n):
    c = 0
    while c < n:
        num = random.randint(MIN_NUM, MAX_NUM)
        if num in ss_list:
            continue
        ss_list.append(num)
        c = c + 1


def sSearch(n):
    total = len(ss_list)
    idx = 0
    cnt = 0
    s_Start = time.time()  # 선형 시간 시작
    s_End = None
    while idx < total:
        if n == ss_list[idx]:
            s_End = time.time()  # 끝
            return idx, cnt, s_Start, s_End
        idx = idx + 1
        cnt = cnt + 1

    return False, cnt, s_Start, time.time()


def B_Search(n):
    bb_list = sorted(ss_list)
    start = 0
    end = len(bb_list) - 1
    cnt = 0
    B_Start = time.time()
    while start <= end:
        mid = (start + end) // 2

        if bb_list[mid] == n:
            B_End = time.time()
            return mid, cnt, B_Start, B_End

        elif bb_list[mid] < n:
            cnt = cnt + 1
            start = mid + 1
        else:
            cnt = cnt + 1
            end = mid - 1

    return False, cnt, B_Start, time.time()


totalNum = int(input("몇개의 난수를 생성할까요:"))
genRandom(totalNum)
print("리스트", len(ss_list), "개 생성")

while True:
    menu = int(input("1.선형검색 2.이진탐색 0.종료:"))
    if menu == 0:
        break
    elif menu == 1:
        num = int(input('찾을 숫자는:'))
        result, cnt, s_Start, s_End = sSearch(num)
        if not result:
            print("검색실패")
        else:
            print("검색성공")
            print("Index= ", result)
            print("Count= ", cnt)
            print("Time= %.20f" % (s_End - s_Start))
    elif menu == 2:
        num = int(input('찾을 숫자는:'))
        result, cnt, B_Start, B_End = B_Search(num)
        if not result:
            print("검색실패")
        else:
            print("검색성공")
            print("Index= ", result)
            print("Count= ", cnt)
            print("Time= %.20f" % (B_End - B_Start))