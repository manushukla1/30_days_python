from loguru import logger
from src.main.databases.mysqlconnecter import MySQLConnection, ReadFromMySQL


class Labour:
    # total_count = 0  #class variable

    def __init__(self, first_name, last_name, wage, role,crud):
        self.first_name = first_name  #instance_variable
        self.last_name = last_name
        self.wage = wage
        self.role = role
        self.crud = crud
        self.__save_to_db(crud)
        # labour.total_count += 1

    def __save_to_db(self,crud):
        query = f"SELECT id from labours WHERE lower(first_name) = '{self.first_name}' AND lower(last_name) = '{self.last_name}'"
        result = crud.read_from_mysql(query)

        if result:  # if labour already exists, return existing id
            logger.info(f"labour already exists with ID: {result[0][0]}")
            return result[0][0]

        insert_query = """
                  INSERT INTO labours (first_name,last_name,wage,role,email)
                  VALUES (%s, %s, %s, %s, %s) """
        logger.info(f"{insert_query}")
        logger.info((self.first_name, self.last_name, self.wage, self.role, None))
        email = self.first_name + " " + self.last_name + "@gmail.com"
        crud.insert_into_mysql(insert_query, (self.first_name, self.last_name, self.wage, self.role,email))
        result = crud.read_from_mysql(query)
        logger.info(f"labour created with ID: {result[0][0]}")
        return result[0][0]

    def login(self):
        pass


import configparser

config = configparser.ConfigParser()
config.read(r"C:\Users\Manu\PycharmProjects\30DaysPython\src\resources\config_file.ini")
mysql_connection_obj = MySQLConnection(config)
mysql_connection_obj.connect()
crud = ReadFromMySQL(mysql_connection_obj.connection)

# manish_obj = Labour("manish", "kumar", 500, "mistri")
# manish_obj.save_to_db(crud)
#
# ramesh_obj = Labour("ramesh", "kumar", 500, "labour",crud)
# ramesh_obj.save_to_db(crud)

shumesh_obj = Labour("shumesh", "nonu", 1000, "mistri",crud)
# shumesh_obj.save_to_db(crud)
#
# print(labour.total_count)  # jab bhi ek naya varaible jaegaa clas phirse chalega toh count reset hojaegaaa broo remember
