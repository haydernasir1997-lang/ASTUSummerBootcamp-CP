t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    suf_val = [0] * n
    suf_idx = [0] * n

    suf_val[n - 1] = a[n - 1]
    suf_idx[n - 1] = n - 1

    for i in range(n - 2, -1, -1):
        if a[i] < suf_val[i + 1]:
            suf_val[i] = a[i]
            suf_idx[i] = i
        else:
            suf_val[i] = suf_val[i + 1]
            suf_idx[i] = suf_idx[i + 1]

    left_min = a[0]
    left_idx = 0

    found = False

    for j in range(1, n - 1):
        if left_min < a[j] and suf_val[j + 1] < a[j]:
            print("YES")
            print(left_idx + 1, j + 1, suf_idx[j + 1] + 1)
            found = True
            break
        if a[j] < left_min:
            left_min = a[j]
            left_idx = j

    if not found:
        print("NO")
