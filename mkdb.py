import sqlite3

conn = sqlite3.connect('database.db')
print("Database opened successfully")

conn.execute('CREATE TABLE allItems (name TEXT, addr TEXT, city TEXT, descrp TEXT, Type TEXT, aid TEXT)')
print ("Table created Successfully") 

conn.execute('CREATE TABLE food (fileid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, addr TEXT, city TEXT, descrp TEXT, Type TEXT, aid TEXT )')
conn.execute('CREATE TABLE hygiene (fileid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, addr TEXT, city TEXT, descrp TEXT, Type TEXT, aid TEXT)')
conn.execute('CREATE TABLE jobs (fileid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, addr TEXT, city TEXT, descrp TEXT, Type TEXT, aid TEXT)')
conn.execute('CREATE TABLE clothes (fileid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, addr TEXT, city TEXT, descrp TEXT, Type TEXT, aid TEXT)')
conn.execute('CREATE TABLE shelter (fileid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, addr TEXT, city TEXT, descrp TEXT, Type TEXT, aid TEXT)')
conn.execute('CREATE TABLE transportation (fileid INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT, addr TEXT, city TEXT, descrp TEXT, Type TEXT, aid TEXT)')
conn.execute('CREATE TABLE userId (wNum TEXT PRIMARY KEY,name TEXT,username TEXT, password TEXT,clubA INTEGER, clubB INTEGER)')

conn.close()
