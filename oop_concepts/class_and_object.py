from loguru import logger
class labour:
    total_count = 0 #class varaible
    def __init__(self,first_name,last_name,wage):
        self.first_name = first_name #instance_variable
        self.last_name = last_name
        self.wage = wage
        labour.total_count += 1


    def save_to_db(self,db_connection):
        pass
        query = "SELECT id from labours WHERE lower(first_name) = %s AND lower(last_name) = %s AND wage = %s"
        result = self.crud.read_from_mysql(query,(self.first_name,self.last_name))
        if result: # if labour already exists, return exisitng id
            logger.info(f"labour already exists with ID: {result[0][0]}")
            return result[0][0]


    def login(self):
        pass



manish_obj = labour("manish","kumar",500)
ramesh_obj = labour("ramesh","kumar",500)
print(labour.total_count) # jab bhi ek naya varaible jaegaa clas phirse chalega toh count reset hojaegaaa broo remember


