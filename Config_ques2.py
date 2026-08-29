from loguru import logger

import configparser

config = configparser.ConfigParser()

config.read(r"C:\Users\Manu\PycharmProjects\30DaysPython\config_file.ini")

student_details = {
    1: ["Math","History"],
    2: ["Biology","Chemistry","History"],
    3: ["Science"]
}

"""
1. iterate dictionary
2. check the len of value
3. if value > 2 then apply discount logic 
4. if  not then return exact price without applying discount
"""

Total_cost_per_student ={}

for key, value in student_details.items():
    cost = 0
    for item in value:
        cost += int(config["BookCost"][item.lower()])

    # if len(value) >= 2:
    #     Apply_discount = cost * 0.1
    #     Total_cost_per_student[key] = cost - Apply_discount
    # else :
    #     Total_cost_per_student[key] = cost

print(Total_cost_per_student)








