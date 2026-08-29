from src.main.databases.mysqlconnecter import *



import configparser


config = configparser.ConfigParser()
config.read(r"C:\Users\Manu\PycharmProjects\30DaysPython\src\resources\config_file.ini")


def main():
    mysql_db_connection = MySQLConnection(config)
    mysql_db_connection.connect()


    crud_operation_obj= ReadFromMySQL(mysql_db_connection.connection)
    final_result=crud_operation_obj.read_from_mysql("select * from labours_table")
    logger.info(f"final_result: {final_result}")
    mysql_db_connection.close()





if __name__ == "__main__":
    main()