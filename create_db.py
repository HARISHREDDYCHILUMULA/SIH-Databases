import sqlite3

conn = sqlite3.connect('database.db')
print ("Opened database successfully")
conn.execute('CREATE TABLE customer_details (customer_id INTEGER PRIMARY KEY AUTOINCREMENT, name varchar, mobile_number INTEGER);')
conn.execute('CREATE TABLE vehicle_details (vehicle_number varchar PRIMARY KEY, customer_id INTEGER, FOREIGN KEY (customer_id) REFERENCES customer_details (customer_id));')
conn.execute('CREATE TABLE provider_details (id INTEGER PRIMARY KEY AUTOINCREMENT, provider_id INTEGER, name TEXT, address TEXT, spot_id INTEGER);')
conn.execute('CREATE TABLE spot_details (spot_id INTEGER PRIMARY KEY, slot_id INTEGER, latitude REAL, longitude REAL, price REAL, monitoring BOOLEAN, FOREIGN KEY (slot_id, latitude, longitude) REFERENCES spot_details (slot_id, latitude, longitude));')
conn.execute('CREATE TABLE availability (spot_id INTEGER, slot_id INTEGER, available BOOLEAN, FOREIGN KEY (spot_id) REFERENCES spot_details (spot_id));')
conn.execute('CREATE TABLE needs (vehicle_number TEXT, latitude REAL, longitude REAL, FOREIGN KEY (vehicle_number) REFERENCES vehicle_details (vehicle_number));')
conn.execute('CREATE TABLE schedule (vehicle_number TEXT, id INTEGER, start_time DATETIME, end_time DATETIME, surge REAL, amount REAL, FOREIGN KEY (vehicle_number) REFERENCES vehicle_details (vehicle_number));')
conn.execute('CREATE TABLE extensions (vehicle_number TEXT, time DATETIME, FOREIGN KEY (vehicle_number) REFERENCES vehicle_details (vehicle_number));')

print ("Table created successfully")
conn.close()
