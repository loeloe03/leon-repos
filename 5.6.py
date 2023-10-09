lst = [1,2,3,4,]

for i in lst:
    if i > i+1:
        lst[i+1],lst[i] = lst[i],lst[i+1]
        