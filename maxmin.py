list = eval(input("Which integers?"))
final = []
j = list[0]
k = list[0]
for i in list:
    if i > j:
        j = i
    elif i < k:
        k = i
final.append(k)
final.append(j)
print(final)

