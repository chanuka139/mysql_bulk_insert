import mysql.connector
import random
import logging


MYSQL_HOST='localhost'
DATABASE_NAME='INS_TEST'
USERNAME='user'
PASS='password'
TABLE_NAME='test'
LOG_FILE_NAME='mysql_bulk_insert.log'

NUM_OF_RECS=10000
POINTER=0

logging.basicConfig(filename=LOG_FILE_NAME, level=logging.DEBUG)

print("Please check "+LOG_FILE_NAME+" for more information and to monitor the executing status of this script.")

logging.debug('The MySQL data entry script started to execute.')
logging.debug('Configuration parameters are, MySQL Host:'+MYSQL_HOST+' Database:'+DATABASE_NAME+' Table:'+TABLE_NAME)
logging.debug(str(NUM_OF_RECS)+' will be added to the table.')

try:
    connection = mysql.connector.connect(host=MYSQL_HOST,
                                         database=DATABASE_NAME,
                                         user=USERNAME,
                                         password=PASS)

    while POINTER < NUM_OF_RECS:
        RAND_NUM1=random.randint(10000, 99999)
        RAND_NUM2=random.randint(10000, 99999)
        RAND_NUM3=random.randint(10000, 99999)
        RAND_NUM4=random.randint(10000, 99999)

        mySql_insert_query = """INSERT INTO """+TABLE_NAME+""" (lastName, firstName, address, city) 
                           VALUES 
                           ('Doe_"""+str(RAND_NUM1)+"""', 'John_"""+str(RAND_NUM2)+"""', 'Singapore_"""+str(RAND_NUM3)+"""', 'Singapore_"""+str(RAND_NUM4)+"""') """

        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
        connection.commit()
        POINTER += 1
        logging.debug("Following values entered to the "+TABLE_NAME+": Doe_"+str(RAND_NUM1)+",John_"+str(RAND_NUM2)+",Singapore_"+str(RAND_NUM3)+",Singapore_"+str(RAND_NUM4)+"So far "+str(POINTER)+" Records were inserted.")
        cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        logging.info("MySQL connection is closed")
        logging.debug("Script completed executing successfully.")
