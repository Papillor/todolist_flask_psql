from flask import render_template, request, redirect, url_for
from app import app
from app.__init__ import cur, conn

@app.route('/')
def index():
    cur.execute("SELECT * FROM todos;")
    todos = cur.fetchall()

    incomplete = [todo for todo in todos if not todo[2]] 
    complete = [todo for todo in todos if todo[2]] 

    return render_template('index.html', incomplete=incomplete, complete=complete)

@app.route('/add', methods=['POST'])
def add():
    todoitem = request.form['todoitem']
    cur.execute("INSERT INTO todos (text, complete) VALUES (%s, %s);", (todoitem, False))
    conn.commit()

    return redirect(url_for('index'))

@app.route('/complete/<id>')
def complete(id):
    cur.execute("UPDATE todos SET complete = %s WHERE id = %s;", (True, id))
    conn.commit()
    return redirect(url_for('index'))