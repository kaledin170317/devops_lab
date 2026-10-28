import os

import psycopg
from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    with psycopg.connect(
        host="db",
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
    ) as connection:
        count = connection.execute(
            """INSERT INTO visits (id, count) VALUES (1, 1)
               ON CONFLICT (id) DO UPDATE SET count = visits.count + 1
               RETURNING count"""
        ).fetchone()[0]

    return f"<h1>Привет! Открытий страницы: {count}</h1>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
