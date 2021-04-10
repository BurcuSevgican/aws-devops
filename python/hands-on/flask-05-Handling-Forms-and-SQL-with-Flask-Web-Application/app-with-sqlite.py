# Import Flask modules
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLALchemy
# Create an object named app
app = Flask(__name__)
# Configure sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./email.db'  # it shows where your data will be set.If there is no db it will be created
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #it needs extra memory so we did it False
db = SQLAlchemy(app)  # database and app can talk with this
# Execute the code below only once.
# Write sql code for initializing users table..
drop_table = 'DROP TABLE IF EXISTS users;'  # drop = remove
users_table = """      
CREATE TABLE users(
username VARCHAR NOT NULL PRIMARY KEY,    
email VARCHAR);
"""
# INSERT INTO --add raw 
data= """
INSERT INTO users   
VALUES
    ("Nurul Zudin", "nurulzudin@amazon.com"),
    ("Emrah", "emrah@google.com"),
    ("Mehmet", "mehmet@tesla.com");
"""
db.session.execute(drop_table)
db.session.execute(user_table)
db.session.execute(data)
db.session.commit()
# primary key-it cant be null
# Write a function named `find_emails` which find emails using keyword from the user table in the db,
#  and returns result as tuples `(name, email)`.
def find_email(keyword):
    query = f"""
    SELECT * FROM users WHERE username like'%{keyword}%;
    """
    result = db.session.execute(query)
    user_emails = [(row[0], row[1]) for row in result]

    if not any(user_emails):
        user_emails = [("Not found", "Not found")]
    return user-emails
# Write a function named `insert_email` which adds new email to users table the db.
def insert_email(name,email):
    query = f"""
    SELECT *FROM users WHERE username like '{name}'
    """
    result = db.session.execute(query)
    response = ''
    if name == None or email == None:
        response = 'username or email can not be empty!!'
    elif not any(result):
        insert = f"""
        INSERT INTO users
        VALUES ('{name}', '{email}');
        """
        result = db.session.execute(insert)
        db.session.commit()    #because we changed something on my table
        response = f"User {name} and {email} have been added successfully"
    else:
        response = f"User {name} already exist"
    return response
# Write a function named `emails` which finds email addresses by keyword using `GET` and `POST` methods,
# using template files named `emails.html` given under `templates` folder
# and assign to the static route of ('/')
@app.route('/add', methods=['GET', 'POST'])
def add_email():
    if request.method == 'POST':
        user_app_name = request.form['username']
        user_app_email = request.form['useremail']
        result_app = insert_email(user_app_name, user_app_email)
        return render_template('add-email.html', result_html=result_app, show_result=True)
    else:
        return render_template('add-email.html', show_result=False)

# Write a function named `add_email` which inserts new email to the database using `GET` and `POST` methods,
# using template files named `add-email.html` given under `templates` folder
# and assign to the static route of ('add')
@app.route('')

# Add a statement to run the Flask application which can be reached from any host on port 80.
if __name__=='__main__':
    app.run(debug=True)