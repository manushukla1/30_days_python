from loguru import logger

numb_list = []
for i in range (1,11):
    if i%2==0:
        numb_list.append(i)
print(numb_list)


numb_list1 =[i for i in range(1,11) if i%2==0]
print(numb_list1)

numb_list2 =["Even" if i%2==0 else "odd" for i in range(1,11)]
print(numb_list2)


