from loguru import logger
import mysql.connector

class MySQLConnection:

    def __init__(self,config):
        self.config = config
        self.connection = None


    def connect(self):
        try:
            self.connection = mysql.connector.connect(host=self.config["mysql_database"]["host"],
                                                      user=self.config["mysql_database"]["user"],
                                                      password=self.config["mysql_database"]["password"],
                                                      database=self.config["mysql_database"]["database"])
            logger.info("mysql connection established")

        except Exception as e:
            logger.error(f"Connection failed to get established {e}")
            raise e

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            logger.info("mysql connection closed")

class ReadFromMySQL:
    def __init__(self,mysql_connection):
        self.connection = mysql_connection

    def read_from_mysql(self,query):
        try:
            cursor = self.connection.cursor()

            cursor.execute(query)
            results = cursor.fetchall()
            logger.info(f"{results}")
            return results
        except Exception as e:
            logger.info(f"{e}")
            raise e
        finally:
            if cursor:
                cursor.close()
                logger.info("mysql  closed")

    def insert_into_mysql(self, query, parameter):
        try:
            cursor = self.connection.cursor()

            logger.info(query)
            logger.info(parameter)

            cursor.execute(query, parameter)

            self.connection.commit()

            logger.info(f"{cursor.rowcount} row(s) inserted")

        except Exception as e:
            logger.info(f"{e}")
            raise

        finally:
            if cursor:
                cursor.close()
                logger.info("mysql closed")




