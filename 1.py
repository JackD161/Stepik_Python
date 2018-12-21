objects = [1,2,3,4,5,6,1,2,3,4,1,3,4,1,12123,24,14,123414,51535426,234412,3,1,2,3]
ans = 0
ans2 = 0
for obj in objects:
    for ind in range(len(objects)-1):
        if obj is objects[ind]:
            ans2 += 1
    if ans2 < 2:
        ans += 1
print (ans)