n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

if k == 0:
    if a[0] == 1:
        print(-1)
    else:
        print(1)

else:
    if k == n or a[k-1] != a[k]:
        print(a[k-1])

    else:
        print(-1)
