import psycopg2

try:
    conn = psycopg2.connect(
        dbname="donna_db",
        user="postgres",
        password="870@Ayush",
        host="localhost"
    )
    print("✅ Connection Successful! Donna has a brain!")
    conn.close()
except Exception as e:
    print(f"❌ Connection Failed: {e}")