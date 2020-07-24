import sys
input = sys.stdin.readline

def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
    
        mx = max(a)
        ans = [ 'a' * (mx + 1) ] * (n + 1)
    
        for i, x in enumerate(a):
            who = 'a' if ans[i][x] == 'b' else 'b'
            ans[i + 1] = ans[i][:x] + who + ans[i][x + 1:]
    
        print('\n'.join(ans))    

main()