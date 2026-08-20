from loguru import logger

import configparser

config = configparser.ConfigParser()

config.read(r"C:\Users\Manu\PycharmProjects\30DaysPython\config_file.ini")

brick_cost = float(config["raw_materials"]["brick_cost"])

def total_Bricks(Length,Breadth,Height):
    total_number_of_rooms = 4
    Construction_Progress = 0
    All_bricks = 0
    while (Construction_Progress <= total_number_of_rooms):
        if Construction_Progress == 0:
            Construction_Progress = Construction_Progress + 1
            pass
        elif Construction_Progress == 1:
            bricks_in_length = Length * (Height * 2)
            total_bricks_in_length_side = bricks_in_length * 2  # opposite wall bro
            bricks_in_breadth = Breadth * (Height * 2)
            total_bricks_in_breadth_side = bricks_in_breadth * 2  # opposite wall bro
            Room_One_total_bricks = total_bricks_in_length_side + total_bricks_in_breadth_side
            All_bricks = All_bricks + Room_One_total_bricks
            Construction_Progress = Construction_Progress + 1
        elif Construction_Progress <= total_number_of_rooms:
            bricks_in_length = Length * (Height * 2)
            total_bricks_in_length_side = bricks_in_length * 2  # opposite wall bro
            bricks_in_breadth = Breadth * (Height * 2)
            total_bricks_in_breadth_side = bricks_in_breadth  # opposite wall bro
            Rest_rooms_total_bricks = total_bricks_in_length_side + total_bricks_in_breadth_side
            All_bricks = All_bricks + Rest_rooms_total_bricks
            Construction_Progress = Construction_Progress + 1

    return All_bricks


def Total_Bricks_Costing(config):
    brick_costing = float(config["raw_materials"]["brick_cost"])
    total_no_of_bricks = total_Bricks(float(config["room_dimension"]["Length"]),float(config["room_dimension"]["Breadth"]),float(config["room_dimension"]["Height"]))
    final_cost = brick_costing * total_no_of_bricks
    return final_cost

logger.info(Total_Bricks_Costing(config))


