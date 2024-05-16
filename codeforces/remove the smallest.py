test_cases = int(input())
for _ in range(test_cases):
    a_length = int(input())
    a = list(map(int,input().split()))
    s = sorted(a)
    for i in range(len(a)-1):
        if abs(s[i]-s[i+1]) > 1:
            print("NO")
            break
    else:
        print("YES")
