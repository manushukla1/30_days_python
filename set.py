# list1 = [1,2,3,4,5,6]
# list2 = [4,5,6,7,8]
# t1 = set(list1)
# t2 = set(list2)
#
# missing_values_t1 = t2.difference(t1)
# print(missing_values_t1)
# missing_values_t2 = t1.difference(t2)
# print(missing_values_t2)


ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
#
# common = set(ar1).intersection(set(ar2)).intersection(set(ar3))
# print(common)
# print(type(common))
output = set()
for num in ar1:
    if num in ar2 and ar3:
        output.append(num)