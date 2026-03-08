from loguru import logger

# labour = ["moti","dhoti","roti","goti"]
#
# # print(labour)
# logger.info(labour[1])
#
# logger.info(labour.append("sotiii"))
# logger.info(labour)
#
# labour_add = ["tusus","clear1", "clear2"]
# labour.extend(labour_add)
# logger.info(labour)
#
# labour.insert(0,"sundervira")
# logger.info(labour)

#Multidimensional list

labour_with_cost = [["Sonu",400] , ["goru",400] ]

logger.info(f"{labour_with_cost[0][0]} is charging {labour_with_cost[0][1]}")
