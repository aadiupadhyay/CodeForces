# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import stdin, stdout
from collections import Counter
def st(): return list(stdin.readline().strip())


def li(): return list(map(int, stdin.readline().split()))
def mp(): return map(int, stdin.readline().split())
def inp(): return int(stdin.readline())
def pr(n): return stdout.write(str(n)+"\n")


mod = 1000000007


def merge(l, left, right):
    i, j, k = 0, 0, 0
    ans = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            l[k] = left[i]
            i += 1
        else:
            ans += (len(left)-i)
            l[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        l[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        l[k] = right[j]
        j += 1
        k += 1

    return ans


def merge_sort(l):
    ans = 0
    if len(l) > 1:
        mid = len(l)//2
        left = l[:mid]
        right = l[mid:]
        ans += merge_sort(left)
        ans += merge_sort(right)
        ans += merge(l, left, right)
    return ans


for _ in range(1):
    n = inp()
    l = li()
    x = list(l)
    ans = merge_sort(l)
    for i in range(1, n+1):
        pr(ans)
        ans += n-1-2*(x[i-1])
