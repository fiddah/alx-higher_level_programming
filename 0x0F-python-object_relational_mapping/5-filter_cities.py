#!/usr/bin/python3
"""
python script that lists all cities from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities
               JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s
               ORDER BY cities.id", (argv[4],))
    rows = c.fetchall()
    print(", ".join(city[0] for city in rows))
    c.close()
    db.close()
