#!/usr/bin/python3


"""
a script that takes in the name of a state as
n argument and lists all cities of that state,
 using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(
        "select cities.name from cities  INNER join states"
        " on  states.id = cities.state_id "
        "where states.name like %s order by cities.id",
        (sys.argv[4],))

    rows = cursor.fetchall()
    print(", ".join(city[0] for city in rows))
    cursor.close()
    db.close()