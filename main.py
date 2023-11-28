from datetime import datetime
from flask import Flask, render_template, request
from controllers.upload import upload_blueprint
import psycopg2



app = Flask(__name__)
# ブループリントの登録
app.register_blueprint(upload_blueprint, url_prefix='/upload')


def connect_to_database():
    """PostgreSQLデータベースに接続"""
    return psycopg2.connect(
        dbname="neondb", 
        user="neon", 
        password="Ehgk5s2OvUKm", 
        host="ep-late-forest-07793227.us-east-2.aws.neon.tech"
    )

#home
@app.route('/')
def index():
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute("SELECT * FROM dummy_table")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', rows=rows)


#run
app.run(host='0.0.0.0', port=81)