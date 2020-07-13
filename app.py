from MySQLdb import *
from flask import Flask, render_template, request, redirect, url_for

con = connect(host='localhost', database='my_DB', user='root', password='sagar')
cursor = con.cursor()

query = 'select * from my_table_2'
cursor.execute(query)
headers = [i[0] for i in cursor.description]
values = []
cursor.execute(query)
data = cursor.fetchall()
for i in data:
    record = {headers[j]: i[j] for j in range(len(headers))}
    values.append(record)
print(values)

app = Flask(__name__,static_url_path = "", static_folder = "static")
@app.route("/")

@app.route("/home", methods=['GET','POST'])
def home():
    query = 'select * from my_table_2'
    cursor.execute(query)
    headers = [i[0] for i in cursor.description]
    values = []
    cursor.execute(query)
    data = cursor.fetchall()
    for i in data:
        record = {headers[j]: i[j] for j in range(len(headers))}
        values.append(record)
    return render_template("home.html",posts=values,title='Home')

@app.route(("/about"))
def about():
    return render_template('about.html',title='About')

@app.route(("/delemp"))
def delemp():
    return render_template('home.html',title='Delete Employee')
@app.route("/addemp", methods=['GET','POST'])
def addemp():
    if request.method == 'POST':
        empno=request.form['empno']
        empname=request.form['empname']
        empplace=request.form['empplace']
        return redirect(url_for("user",empno=empno,empname=empname,empplace=empplace))
    else:
        return render_template('addemp.html',title='Add Employee')
@app.route("/<empno>,<empname>,<empplace>")
def user(empno,empname,empplace):
    value=(empno,empname,empplace)
    insert_query='insert into my_table_2 values {}'.format(str(value))
    cursor.execute(str(insert_query))
    con.commit()
    values = []
    query = 'select * from my_table_2'
    cursor.execute(query)
    data = cursor.fetchall()

    for i in data:
        record = {headers[j]: i[j] for j in range(len(headers))}
        values.append(record)

    return render_template("home.html",posts=values,title='Home')


if __name__=='__main':
    app.run(debug=True)