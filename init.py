
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('drop table if exists todo')
cursor.execute('create table todo \
    (id INTEGER PRIMARY KEY AUTOINCREMENT,\
    name varchar(20), \
    urgency int(4) default 0, \
    importancy int(4) default 0,\
    done int(1) default 0, \
    create_time datetime default current_timestamp)')
cursor.close()
conn.commit()
conn.close()