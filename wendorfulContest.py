t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    if max(a)==100:
        print("YES")
    else:
        print("NO")
