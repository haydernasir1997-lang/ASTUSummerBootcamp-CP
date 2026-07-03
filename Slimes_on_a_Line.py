n = int(input())
for i in range(n):
    m = int(input())
    nums = sorted(list(map(int,input().split())))
    if m % 2 == 0:
        x = (nums[-1] + nums[0]) // 2
        first = x - nums[0]
        last = nums[-1] - x 
        print(max(first,last))
    else:
        x = (nums[-1] + nums[0]) // 2  
        first = x - nums[0]
        last = nums[-1] - x 
        print(max(first,last))
