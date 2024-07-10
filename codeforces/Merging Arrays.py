n_leng, m_leng = map(int, input().split())
n = list(map(int, input().split()))
m = list(map(int, input().split()))
ans = []

i = 0
j = 0

while i < n_leng and j < m_leng:
    if n[i] <= m[j]:
        ans.append(n[i])
        i += 1
    else:
        ans.append(m[j])
        j += 1

if i != n_leng:
    ans.extend(n[i:])

if j <m_leng:
    ans.extend(m[j:])
print(" ".join(map(str, ans)))
