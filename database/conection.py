import MySQLdb

class Conexao:
    con = MySQLdb.connect(host='35.247.242.36',
                          database='apipython', user='root', password='Lucas88006949')
    cursor = con.cursor()