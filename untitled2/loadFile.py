import os
from flask import Flask,render_template,request
from flaskext.mysql import MySQL
from flask import Flask, jsonify, request
import uuid




app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'transinfo2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL(app)

mysql.init_app(app)

__author__ = 'jess'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, '/Users/jessicacotrina/Desktop/file')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")

@app.route("/prueba", methods=['GET'])
def prueba():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM AccidentCondition''')
    rv = cursor.fetchall()
    return jsonify(rv)

@app.route("/LoadData", methods=['POST'])
def add():

    conn = mysql.connect()
    cursor = conn.cursor()
    fileName = str(uuid.uuid4())
    # request.form['fileName']
    fecha = request.form['fecha']
    path = request.form['path']
    idAccidentFK = request.form['idAccidentFK']
    #
    print ("filename",fileName)
    print ("fecha", fecha)
    print ("path", path)
    print ("idAccidentFK", idAccidentFK)

    target = os.path.join(APP_ROOT, '/Users/jessicacotrina/Desktop/file')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    #

    path = destination
    cursor.execute('''INSERT INTO CollisionDiagram (fileName, fecha, path,idAccidentFK) VALUES (%s, %s, %s, %s)''',(fileName,fecha,path,idAccidentFK))
    conn.commit()
    return "Done"


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(port=5000, host='0.0.0.0')