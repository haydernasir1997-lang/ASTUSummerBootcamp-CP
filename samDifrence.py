t=int(input())
for i in range(t):
    n = int(input())
    s = input()
    want = s.count(s[len(s)-1])
    final = n - want
    print(final)
