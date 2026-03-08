from operator import concat

from loguru import logger
import math

# lg_of_land = 100
# bd_of_land = 300
#
# total_area = lg_of_land * bd_of_land
# logger.info(f"total_area of land is {total_area} sq. ft.")

#modulo operator
# logger.info(15%6)

#floor division
# logger.info(15//6)
# logger.info(math.floor(15/6))
# logger.info(math.ceil(15/7))

a = "1"
b ="2"
# print(int(a)+int(b)) #type casting
print(a+b) #concatenate

#user input

lg_of_land = float(input("PLease enter length of land "))
bd_of_land = float(input("PLease enter breadth of land "))
# print(type(lg_of_land),type(bd_of_land))
total_area = abs (lg_of_land * bd_of_land)
print(total_area)