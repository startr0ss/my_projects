import sqlite3 as sql

conn = sql.connect('Database.db')
cursor = conn.cursor()

def checkTable(nameTbl):
    if nameTbl == 'HOMA_errors':
        cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name LIKE 'HOMA_errors'")
        return cursor.fetchone()

def crtTable(nameTbl):
    if nameTbl == 'HOMA_errors':
        cursor.execute("CREATE TABLE HOMA_errors (nameHOMA text, minValue float, averageValue float, maxValue float)")

def insertHOMA(nameTbl, nameHOMA, values):
    if nameTbl == 'HOMA_errors':
        cursor.execute(f"INSERT INTO HOMA_errors VALUES (?, ?, ?, ?)", (nameHOMA, values[0], values[1], values[2]))
        conn.commit()

def updateTable(nameTbl, nameHOMA, values):
    if nameTbl == 'HOMA_errors':
        cursor.execute(f"UPDATE HOMA_errors SET minValue = ? WHERE nameHOMA = ?", (values[0], nameHOMA))
        cursor.execute(f"UPDATE HOMA_errors SET averageValue = ? WHERE nameHOMA = ?", (values[1], nameHOMA))
        cursor.execute(f"UPDATE HOMA_errors SET maxValue = ? WHERE nameHOMA = ?", (values[2], nameHOMA))
        conn.commit()

def slctTable(nameTbl):
    if nameTbl == 'HOMA_errors':
        return cursor.execute("SELECT * FROM HOMA_errors")

def showTable(nameTbl):
    if nameTbl == 'HOMA_errors':
        table = slctTable('HOMA_errors')
        for row in table:
            print(row[0], row[1], row[2], row[3])

def slctRow(nameTbl, nameHOMA):
    if nameTbl == 'HOMA_errors':
        cursor.execute("SELECT * FROM HOMA_errors WHERE nameHOMA = :nameHOMA", {"nameHOMA": nameHOMA})
        return cursor.fetchone()