import psycopg2

connection = psycopg2.connect(
    host = 'localhost',
    user= 'postgres',
    password = '02212026',
    dbname = 'polban'
)

cursor = connection.cursor()


cursor.execute ("SELECT nim , nama  from mahasiswa")
data = cursor.fetchall()

print(data[0])
    
cursor.close()
connection.close()