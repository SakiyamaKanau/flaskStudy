from flask import Blueprint, render_template, request
from datetime import datetime
from models.database import connect_to_database


upload_blueprint = Blueprint('upload', __name__)


@upload_blueprint.route('/upload')
def upload():
    return render_template('upload.html')


@upload_blueprint.route('/uploadFile', methods=['POST'])
def uploadFile():
    file = request.files['file']
    if not file:
        return 'ファイルがアップロードされていません', 400
    file_content = file.stream.read().decode("utf-8")
    process_csv_data(csv.reader(file_content.splitlines()))
    return 'ファイルがアップロードされ、データが登録されました'

def convert_date_format(japanese_date):
  date_obj = datetime.strptime(japanese_date, '%Y年%m月%d日')
  return date_obj.strftime('%Y-%m-%d')


def process_csv_data(csv_reader):
    """CSVデータを処理してデータベースに挿入"""
    conn = connect_to_database()
    cur = conn.cursor()
    next(csv_reader)  # ヘッダ行をスキップ

    for row in csv_reader:
        #年の表記揺れを修正
        row[3] = convert_date_format(row[3])  
        cur.execute("INSERT INTO dummy_table (name, name_kana, age, birth_date, gender, blood_type, email, phone_number, mobile_phone_number, postal_code, address, company_name, credit_card_number, card_expiry, my_number) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", row)

    conn.commit()
    cur.close()
    conn.close()


