length_home = 80
breadth_home = 60

length_land = 100
breadth_land = 100

length_garden = 100
breadth_garden = 20
cost_of_grass = 10

def calcualte_area(length,breadth):
    return(length*breadth)

area_of_home = calcualte_area(length_home,breadth_home)
area_of_land = calcualte_area(length_land,breadth_land)
area_of_garden = calcualte_area(length_garden,breadth_garden)

def cost_of_grassing(area_of_land,area_of_home,area_of_garden,cost_of_grass):
    cost = (area_of_land - (area_of_home + area_of_garden))*cost_of_grass
    return cost

costing = cost_of_grassing(area_of_land,area_of_home,area_of_garden,cost_of_grass)
print(costing)