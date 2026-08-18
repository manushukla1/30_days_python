from loguru import logger

# labour_with_cost = {"Mahesh":500 , "Ramesh":199 , "Jagmohan":450 , "Mithu":790}

# update labour_with_cost["Monu padey"] = 100000 - ye ek new vlaue add hogi at last

# logger.info(labour_with_cost.items())
# logger.info(labour_with_cost.keys()) --- ye list return karega only keys aeengi
# logger.info(labour_with_cost.values())


# for keys in labour_with_cost:
#     print(labour_with_cost[keys])

# for keys in labour_with_cost:
#     logger.info(f"{keys}, {labour_with_cost[keys]}")

labour_with_cost = {
    "Mahesh": 500,
    "Ramesh": 400,
    "Mithilesh": 400,
    "Sumesh": 300,
    "Jagmohan": 1000,
    "Rampyare": 800
}

absent_days = {
    "Mahesh": 3,
    "Ramesh": 0,
    "Mithilesh": 0,
    "Sumesh": 0,
    "Jagmohan": 7,
    "Rampyare": 0
}
# total_labour_cost = 0
# total_working_days = 50
# for labour in labour_with_cost:
#         total_labour_cost = total_labour_cost +  labour_with_cost[labour]*(total_working_days-absent_days[labour])
#
# print(total_labour_cost)

# total = 0
# for labour in labour_with_cost:
#     total = total + labour_with_cost[labour]
# print(total)
#
# total_final = (50 * total) - ((7*labour_with_cost["Jagmohan"]) + (3*labour_with_cost["Mahesh"]))
# print(total_final)





