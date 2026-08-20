from loguru import logger

import configparser

config = configparser.ConfigParser()

config.read(r"C:\Users\Manu\PycharmProjects\30DaysPython\config_file.ini")

brick_cost = float(config["raw_materials"]["brick_cost"])
logger.info(f"brick cost: {brick_cost}")

def total_no_of_bricks1(length,breadth,height):
    no_of_bricks_in_length_side = length * (height*2)
    total_no_of_bricks_in_length_side = no_of_bricks_in_length_side *2      # opposite wall bro
    no_of_bricks_in_breadth_side = breadth * (height * 2)
    total_of_bricks_in_breadth_side = no_of_bricks_in_breadth_side * 2  # opposite wall bro

    total_bricks = total_of_bricks_in_breadth_side + total_no_of_bricks_in_length_side
    return total_bricks


def  total_cost_for_bricks(config):
    brick_cost = float(config["raw_materials"]["brick_cost"])
    total_no_of_bricks = total_no_of_bricks1(15,15,10)
    final_cost = brick_cost * total_no_of_bricks
    return final_cost

result = total_cost_for_bricks(config)

logger.info(f"total cost: {result}")