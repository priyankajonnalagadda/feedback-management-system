from flask import Flask, render_template, request, redirect
from database import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    feedback = request.form['feedback']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO feedback (name, feedback) VALUES (%s, %s)', (name, feedback))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/view')

@app.route('/view')
def view_feedback():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM feedback')
    feedbacks = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('view.html', feedbacks=feedbacks)

if __name__ == '__main__':
    app.run(debug=True)
 
