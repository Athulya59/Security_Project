from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Hello@12345'
app.config['MYSQL_DB'] = 'test'
app.config['MYSQL_HOST'] = 'localhost'

mysql=MySQL(app)

@app.route('/')
def Home():
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM pin")
	fetchdata=cur.fetchall()
	cur.close
	return render_template('home.html', data=fetchdata)


if __name__ == '__main__':
	app.run(debug=True)
