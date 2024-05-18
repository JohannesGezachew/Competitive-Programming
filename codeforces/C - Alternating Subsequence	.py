test_case = int(input())

for _ in range(test_case):
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    current_max = a[0]

    for i in range(1, n):

        if (a[i] > 0) == (a[i - 1] > 0):
            current_max = max(current_max, a[i])
        else:
            result += current_max

            current_max = a[i]
    
    result += current_max
    
    print(result)
