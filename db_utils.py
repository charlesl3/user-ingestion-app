import random
from faker import Faker
import mysql.connector

fake = Faker()

def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Liuchang!!123',
        database='users_app'
    )

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_user():
    name = fake.name()
    age = random.randint(18, 100)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    cursor.close()
    conn.close()
    return name, age

def count_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return count

def insert_manual_user(name, age):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, age FROM users")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

