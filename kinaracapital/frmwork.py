from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'kinarastudents.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.route('/api/students', methods=['GET'])
def get_students():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))

    conn = connect_db()
    cursor = conn.cursor()

    offset = (page - 1) * page_size
    cursor.execute(f'SELECT * FROM students LIMIT {page_size} OFFSET {offset}')
    students = cursor.fetchall()

    conn.close()

    return jsonify(students)

@app.route('/api/students/filter', methods=['GET'])
def filter_students():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 10))
    filter_criteria = request.args.get('filter_criteria', '')

    conn = connect_db()
    cursor = conn.cursor()

    offset = (page - 1) * page_size
    cursor.execute(f"SELECT * FROM students WHERE name LIKE '%{filter_criteria}%' LIMIT {page_size} OFFSET {offset}")
    filtered_students = cursor.fetchall()

    conn.close()

    return jsonify(filtered_students)

if __name__ == '__main__':
    app.run()
