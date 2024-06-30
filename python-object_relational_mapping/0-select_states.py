#!/usr/bin/python3
"""lists all states"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host='localhost',
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306
    )
    ptr = db.cursor()
    ptr.execute('SELECT * FROM states ORDER BY id ASC')
    rows = ptr.fetchall()
    for row in rows:
        print(row)
    ptr.close()
    db.close()
