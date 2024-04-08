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


@app.route('/account_view')
def home():
    return render_template('show_accounts.html')
    conn.execute(text("select * from accounts"), request.form)
    conn.commit()
    return render_template('show_accounts.html')


@app.route('/create_account', methods = ['POST'])
def create_account():
    conn.execute(text("INSERT INTO accounts VALUES (:id, :username, :email, :password)"), request.form)
    conn.commit()
    return render_template('create_account.html')


@app.route('/filter', methods=['GET'])
def filter():
    return render_template('filter.html')


@app.route('/filter', methods = ['POST'])
def filter_accounts():
    x = request.form['id']
    account = conn.execute(text(f'select * from accounts id type = {x}'))
    conn.execute(text(f"select * from boats where ID = {x}"), request.form)
    conn.commit()
    return render_template('filter.html', boat_info=boat)


if __name__ == '__main__':
    app.run(debug=True)
    # ... start the app in debug mode. In debug mode,
    # server is automatically restarted when you make changes to the code


    