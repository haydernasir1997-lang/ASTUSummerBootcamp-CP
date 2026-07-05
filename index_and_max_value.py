t = int(input())  

for _ in range(t):
    n, m = map(int, input().split()) 
    arr = list(map(int, input().split()))
    
    current_max = max(arr)  
    
    results = []
    
    for _ in range(m):
        op, l, r = input().split()
        l = int(l)
        r = int(r)
        
       
        if l <= current_max <= r:
            if op == '+':
                current_max += 1
            else: 
                current_max -= 1
        
        results.append(str(current_max))
    
    print(' '.join(results))
