from flask import Flask, jsonify
import mysql.connector


app = Flask(__name__)


def professionals_data():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'professionals'
    }
    connection = mysql.connector.connect(**config)

    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT Name, Contact, Specialization FROM professionals_data')

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results


@app.route('/')
def index():
    return jsonify({'professionals Data': professionals_data()})


if __name__ == '__main__':
    app.run(host='0.0.0.0')