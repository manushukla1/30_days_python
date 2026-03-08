from loguru import logger
# lg_of_land = float(input("PLease enter length of land "))
#
# if lg_of_land < 100:
#     logger.info(f"{lg_of_land} is less than 100 you can't build a home in this size")
#     if lg_of_land > 50:
#         logger.info(f"{lg_of_land} is greater than 50 we can help you design it ")
#
# elif lg_of_land > 300:
#     logger.info(f"You can build two building with {lg_of_land} sq. ft.")
#
# else:
#     logger.info(f"lets get on call")

Enter_a_number = int(input("Please Enter a number: "))
Check = Enter_a_number%2
if Check == 0:
    logger.info(f"{Enter_a_number} is Even")

else:
    logger.info(f"{Enter_a_number} is Odd")


