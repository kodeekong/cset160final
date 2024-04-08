from flask import Flask, render_template, request, redirect
from sqlalchemy import create_engine, text

app = Flask(__name__)
# Flask uses this argument to determine the root path of the application so that it later can find resource files
# relative to the location of the application.
connection = 'mysql://root:cset155@localhost/exam'
engine = create_engine(connection, echo=True)
conn = engine.connect()


@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/')
def register(name):
    return render_template('user.html', username = name)

# @app.route('/account_view')


# @app.route('/create_account', methods = ['POST'])
def create_account():
    conn.execute(text("INSERT INTO accounts VALUES (:id, :name, :email, :username, :password)"), request.form)
    conn.commit()
    return render_template('createBoat.html')

if __name__ == '__main__':
    app.run(debug=True)
    # ... start the app in debug mode. In debug mode,
    # server is automatically restarted when you make changes to the code