import MySQLdb

class Conexao:

    con = MySQLdb.connect(host='',
                          database='', user='', password='')

    cursor = con.cursor()