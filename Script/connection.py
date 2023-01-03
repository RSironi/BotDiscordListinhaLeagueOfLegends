import mysql.connector
import config as cf

con = mysql.connector.connect(
    host=cf.HOST, database=cf.DATABASE, user=cf.USER, password=cf.PASSWORD
)
cursor = con.cursor()
