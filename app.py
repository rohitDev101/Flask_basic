from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import generate_password_hash
import time
from decouple import config


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

userID = config('userID',default='')
password = config('password',default='')


st = time.time()
generate_password_hash('@password12343', 13)
et = time.time()
time_elapsed = round((et - st), 2)
print(" time taken : %gs" % time_elapsed)
print ('start %d, end %d' % (st, et))

@app.route('/success/<name>')
def success(name):
    print(userID, password)
    return 'welcome %s !!!' % name

@app.route('/login-page')
def loginPage():
    return render_template('login-page.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name="%s123" % user))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return "This is home!"

if __name__ == "__main__":
    app.run(debug=True)