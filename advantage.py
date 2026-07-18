t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    srt = sorted(nums)
    maximum = srt[-1]
    second_max = srt[-2]

    ans = []
    for i in nums:
        if i == maximum:
            ans.append(i-second_max)
        else:
            ans.append(i-maximum)
    print(*ans)


    
