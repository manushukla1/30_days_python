from loguru import logger

for i in range(5):
    print((5-i) * "* ")


labour_name = ["sonu", "goru","donu","monu", "chonu","gonu"]



for name in range(len(labour_name)):
    print(labour_name[name])


for name in range(len(labour_name)):
    logger.info(f"labour {name+1} name is {labour_name[name]}")