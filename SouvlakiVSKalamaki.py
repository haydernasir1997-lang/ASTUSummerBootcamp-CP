t = int(input())
for _ in range(t):
    n = int(input())
    lis = list(map(int, input().split()))
    lis.sort()
    l = 1
    while l < n-1:
        if lis[l]==lis[l+1]:
            l+=2
        else:
            print("NO")
            break
    else:
        print("YES")
