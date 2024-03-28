s = list(map(int,input().split()))
list_d = {}
rst = []
for i in s:
    if i in list_d:
        list_d[i] += 1
    else:
        list_d[i] = 1
for key, value in list_d.items():
    if value >= 3:
        rst.append(key)
print(rst)