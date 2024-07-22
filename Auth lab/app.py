from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session 
import pyrebase
Config = {
  "apiKey": "AIzaSyAE99ExAgUArKsdIw7A55on6haDaJGs3tw",
  "authDomain": "auth-lab-1451a.firebaseapp.com",
  "projectId": "auth-lab-1451a",
  "storageBucket": "auth-lab-1451a.appspot.com",
  "messagingSenderId": "414219816042",
  "appId": "1:414219816042:web:41e631f3510c99498e0e13",
"databaseURL":"https://auth-lab-1451a-default-rtdb.europe-west1.firebasedatabase.app/"

}
firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db = firebase.database()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods = ['GET', 'POST'])
def signUp():
  if request.method == 'POST':
    full_name = request.form['full_name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    try:
      user = {'email' : email, 'username': username, 'full_name': full_name}
      session['user'] = auth.create_user_with_email_and_password(email, password)
      uid = session['user']['localId']
      db.child('Users').child(uid).set(user)
      return redirect(url_for('home'))
    except:
      error = "Authentication failed"
      return redirect(url_for("error"))
  return render_template("signup.html")



@app.route('/sign-in', methods=['GET','POST'])
def signIn():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    try:
      session['user'] = auth.sign_in_with_email_and_password(email, password)
      return redirect(url_for('home'))
    except:
      error = "Authentication failed"
      return redirect(url_for("error"))
  return render_template("signin.html")

@app.route('/display')
def display():
  if session['user'] != None:
    return render_template("display.html", quotes = db.child('Quotes').get().val())
  else:
    return redirect(url_for('signIn'))
@app.route('/home', methods = ['GET','POST'])
def home():
  if request.method == 'POST':
    quote = request.form['quote']
    speaker = request.form['speaker']
    session['speaker'] = speaker
    session['quote'] = quote
    quote_info= {'said_by' : speaker,'quote': quote, 'uid' : session['user']['localId']}
    db.child('Quotes').push(quote_info)
    return redirect(url_for('thanks'))
  return render_template('home.html')

@app.route('/thanks')
def thanks():
  if session['user'] != None:
    quote = session['quote']
    speaker = session['speaker']
    return render_template("thanks.html",quote = quote, speaker = speaker)
  else:
    return redirect(url_for('signIn'))

@app.route('/sign-out')
def signOut():
  session['user']=None
  auth.current_user = None
  return redirect(url_for('signIn'))
@app.route('/error.html')
def error():
  return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)