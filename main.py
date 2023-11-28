from flask import Flask, render_template
from controllers.upload import upload_blueprint
from models.database import connect_to_database


app = Flask(__name__)
app.register_blueprint(upload_blueprint, url_prefix='/upload')

#ホーム画
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