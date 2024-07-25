from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session 
import pyrebase
Config = {
  "apiKey": "AIzaSyDJVv_KgpaDVjnOpDpYRqF03NSe0GD2v30",
  "authDomain": "first-project-dd7f2.firebaseapp.com",
  "projectId": "first-project-dd7f2",
  "storageBucket": "first-project-dd7f2.appspot.com",
  "messagingSenderId": "877500103288",
  "appId": "1:877500103288:web:722839df0e6b7ab65e0b8d",
  "databaseURL":"https://first-project-dd7f2-default-rtdb.europe-west1.firebasedatabase.app/"
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
      return redirect(url_for('place'))
    except:
      return "Authentication failed"
  return render_template("signup1.html")



@app.route('/signin', methods=['GET','POST'])
def signIn():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    try:
      session['user'] = auth.sign_in_with_email_and_password(email, password)
      return redirect(url_for('place'))
    except:
      error = "Authentication failed"
      return redirect(url_for("place"))

  return render_template("signin1.html") 


@app.route('/xxx')
def display():
  if session['user'] != None:
    return render_template(".html", quotes = db.child('Quotes').get().val())
  else:
    return redirect(url_for('signIn'))
@app.route('/home', methods = ['GET','POST'])
def place():
  if request.method == 'POST':
    quote = request.form['quote']
    speaker = request.form['speaker']
    session['speaker'] = speaker
    session['quote'] = quote
    quote_info= {'said_by' : speaker,'quote': quote, 'uid' : session['user']['localId']}
    db.child('Quotes').push(quote_info)
    return redirect(url_for('place'))
  return render_template('place.html')


@app.route('/journey')
def journey():
  if session['user'] != None:
    quote = session['quote']
    speaker = session['speaker']
    return render_template("journey.html",quote = quote, speaker = speaker)
  else:

    return redirect(url_for('signIn'))
  return render_template("signup1.html")


@app.route('/sign-out')
def signOut():
  session['user']=None
  auth.current_user = None
  return redirect(url_for('signIn'))
@app.route('/london')
def london():
  return render_template('london.html')

@app.route('/NYC')
def NYC():
  return render_template('NYC.html')

@app.route('/paris')
def paris():
  return render_template('paris.html')

@app.route('/garden')
def garden():
  return render_template("garden.html")  
@app.route('/museum')
def museum():
  return render_template("museum.html")  

@app.route('/beaches')
def beaches():
  return render_template("beaches.html")  
@app.route('/dangerous')
def danger():
  return render_template("danger.html")  


@app.route('/update/<place>', methods=["GET","POST"])
def update(place):
  if request.method=="GET":
    place={
    "the_place":place
    }
    uid = session['user']['localId']
    db.child("Users").child(uid).update(place)
    return render_template("update.html")

  else:
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
  uid = session['user']['localId']
  profile=db.child("Users").child(uid).get().val()
  return render_template('profile.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)
