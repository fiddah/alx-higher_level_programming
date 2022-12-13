#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the states
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states` WHERE name LIKE %s ORDER BY id ASC",
              (argv[4],))
    [print(row) for row in c.fetchall()]
