import mysql.connector

db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='9876',
    database='task_db'
)

cursor = db_connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Task (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task_name VARCHAR(200) NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    result TEXT
)
""")
db_connection.commit()
cursor.close()
db_connection.close()
