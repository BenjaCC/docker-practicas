import os
import time
import psycopg2
from flask import Flask

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )

def init_db():
    for _ in range(10):
        try:
            conn = get_conn()
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS visitas "
                "(id SERIAL PRIMARY KEY, fecha TIMESTAMP DEFAULT NOW())"
            )
            conn.commit()
            cur.close()
            conn.close()
            return
        except psycopg2.OperationalError:
            time.sleep(2)
    raise RuntimeError("No se pudo conectar a la base de datos")

@app.route("/")
def index():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO visitas DEFAULT VALUES")
    cur.execute("SELECT COUNT(*) FROM visitas")
    total = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return f"<h1>Hola desde Flask + PostgreSQL</h1><p>Visitas: {total}</p>"

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
