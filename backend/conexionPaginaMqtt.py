from flask import Flask, jsonify
from flask_mysqldb import MySQL
#hola
app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'S3samio'
app.config['MYSQL_DB'] = 'prueba'

mysql = MySQL(app)

@app.route('/')
def home():
    return 'Conexión a MySQL funcionando'

@app.route('/usuarios')
def obtener_usuarios():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM usuarios")
    data = cursor.fetchall()
    cursor.close()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
