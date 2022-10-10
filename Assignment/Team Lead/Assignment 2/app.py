 
import ibm_db

from flask import Flask, render_template, request

app = Flask(__name__)

conn = ibm_db.connect("DATABASE=bludb ; HOSTNAME=8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30120;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=zsb20612;PWD=jZKZAs5ou1zHS6IO;", '', '')

 


@app.route('/')
def home():
    return render_template('home.html',msg = "Welcome to Home Page")


@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route("/signup_action", methods=["GET", "POST"])
def signup_action():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        password = request.form['password']
        email = request.form['email']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipcode']
        fullname = name+" "+lastname

        """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        sql = "select *from users where uname =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, fullname)
        ibm_db.execute(stmt)
        user_checkIn = ibm_db.fetch_assoc(stmt)
        if user_checkIn:
            return render_template('msg.html', msg="You are already User")
        else:
            insert_sql = "INSERT INTO users VALUES(?,?,?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, fullname)
            ibm_db.bind_param(prep_stmt, 2, password)
            ibm_db.bind_param(prep_stmt, 3, email) 
            ibm_db.bind_param(prep_stmt, 4, address)
            ibm_db.bind_param(prep_stmt, 5, city)
            ibm_db.bind_param(prep_stmt, 6, state)
            ibm_db.bind_param(prep_stmt, 7, zipcode)
            ibm_db.execute(prep_stmt)
        
        return render_template("msg.html",msg="Registered Successfully")
    return 
     

@app.route("/about")
def about():
    return render_template("about.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8088, debug="True")
