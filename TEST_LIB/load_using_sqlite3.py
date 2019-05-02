import sqlite3

conn = sqlite3.connect('my_database.db')
c = conn.cursor()
print("Database opened successfully.")

#conn.execute('''create table Names (id int NOT NULL,
#									fname varchar(20),
#									mname varchar(20),
#									lname varchar(20),
#									primary key (id))''')
#print('Table created successfully.')

#c.execute('insert into Names values(1,"Utkarsh","","Singh")')

conn.commit()

for row in c.execute('SELECT * FROM Names'):
        print(row)
conn.close()

print('Database closed successfully.')