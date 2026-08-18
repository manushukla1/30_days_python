from loguru import logger
labour_with_cost = {
    "Mahesh": 500,
    "Ramesh": 400,
    "Mithilesh": 400,
    "Sumesh": 300,
    "Jagmohan": 1000,
    "Rampyare": 800
}
print(labour_with_cost)
# print(labour_with_cost.get("Mahesh1", "Labour not found")) -- # none type hnalde hojaegaa yaha
# print(labour_with_cost.get("Mahesh1")) -- # bhai ye errror dega but ye handle karne ke liye hum get method ka use karenge jisme default value pass karenge agar key nahi mile to.
#
print(labour_with_cost.keys())
print(labour_with_cost.values())
print(labour_with_cost.items())

#update method
# (labour_with_cost.update({"Mahesh": 600, "Ramesh": 500, "Mithilesh": 500, "Sumesh": 400, "Jagmohan": 1200, "Rampyare": 1000}))
# print(labour_with_cost)
# New_dict =  {"Mahesh": 600, "Ramesh": 500, "Mithilesh": 500, "Sumesh": 400, "Jagmohan": 1200, "Rampyare": 1000}
# final_dict = {**labour_with_cost, **New_dict}  # another way of printing it
# print(final_dict)


# print(labour_with_cost.pop("Mahesh"))  # pop method will remove the key and value from the dictionary and return the value of the key which is removed.
#
# print(labour_with_cost.pop("Ramesh"))
# print(labour_with_cost.popitem())  # popitem method will remove the last key and value from the dictionary and return the key and value of the last item which is removed.
# print(labour_with_cost.keys())
#
# #copy method
#
# new_labour_cost = labour_with_cost.copy()
# print(id(new_labour_cost))
# print(id(labour_with_cost))

#
# labour_with_cost = { key:labour_with_cost.get(key)+100 for key in labour_with_cost}
# print(labour_with_cost)
#
# labour_with_cost = { key:labour_with_cost.get(key)+100 if labour_with_cost.get(key) <1000 else labour_with_cost.get(key) for key
#                      in labour_with_cost}
# print(labour_with_cost)
#
# #IN method - in list vs dictionary
#
#
# name = "ManuShukla"
# letter_count = {}
#
# for char in name:
#     if char in letter_count:
#         letter_count[char] += 1
#     else:
#         letter_count[char] = 1
#     print(letter_count)


# name = "ManuShukla"
#
# unique_char = []
#
# for char in name:
#     if char not in unique_char:
#         unique_char.append(char)
#
# for char in unique_char:
#     print(char , name.count(char))
#