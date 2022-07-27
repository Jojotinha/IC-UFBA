num = input('Digite seus valores\n>>>')
list1 = num.split()
list2 = []
for i in list1:
    n = float(i)
    list2.append(n)
mean = str(sum(list2)/len(list2)).replace('.',',')
print('A média é igual: {}'.format(mean))
