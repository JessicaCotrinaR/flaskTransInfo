from flask import Flask
from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'transinfo2'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)

@app.route('/prueba')

def prueba():
    #return render_template('index.html')
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute('''SELECT * FROM Accident''')
    rv = cursor.fetchall()
    return str(rv)

    # printthis = ""
	# for i in rv:
	# 	printthis += i + "<br>"
    #
	# return printthis

if __name__ == '__main__':
    app.run(debug=True)
