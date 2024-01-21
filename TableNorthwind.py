import pyodbc

connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=ORKHAN;Database=Northwind;Trusted_Connection=yes;')

cursor = connection_to_db.cursor()

cursor.execute('SELECT * FROM Customers')

while True:
    row = cursor.fetchone()
    if not row:
        break
    print('Государство: ' + row.Country, ', город: ' +  row.City)

connection_to_db.close()
