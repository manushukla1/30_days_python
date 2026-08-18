# test_tuple = ([5,6],[6,7,8,9],[3])
# result = []
#
# # for num in test_tuple:
# #     new_variable = tuple(num)
# #     result = result + (new_variable)
# # print(result)
#
# for lst in test_tuple:
#    result = result + lst
# print(tuple(result))


tuple1=(10,2,3,5)
tuple2=(3,6,4,3)
output = ()

for i in range(len(tuple1)):
    result = tuple1[i] ** tuple2[i]
    output = output + (result,)

print(output)

