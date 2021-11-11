n = 5
if n == 1:
    print(1)
dfs = []
dfs.append(1)
dfs.append(2)
i = 2
while i < n:
    dfs.append(0)
    dfs[i] = dfs[i-1] + dfs[i-2]
    i = i + 1
print(dfs[n-1])