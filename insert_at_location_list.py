from loguru import logger
lst1 = [202, 165, 89, 76, 12]
number_to_insert = 15

if len(lst1)  == 0 or number_to_insert < lst1[-1]:
    lst1.append(number_to_insert)
else:
    index = 0
    for number in lst1:
        if number > number_to_insert:
            index = index +1
        else:
            index = index
print(index)
lst1.append(None)
# print(lst1)

for i in range(len(lst1)-1,index,-1):
    lst1[i] = lst1[i-1]
    print(lst1)
    lst1[index] = number_to_insert

print(lst1)