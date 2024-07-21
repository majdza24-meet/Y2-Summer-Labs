from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey' 

fortunes = ["Luck seemed to follow her like a shadow","Sometimes, all you need is a little luck to change your fortunes.","With a stroke of luck, we found the missing keys.","Every roll of the dice seems to go my way.","I feel blessed to have such fortunate circumstances.","Somehow, against all odds, everything turned out perfectly.","The lucky charm I carry always brings me good fortune."," I stumbled upon a lucky penny just when I needed it most.","Finding a four-leaf clover made my day!"," Luck is what happens when preparation meets opportunity."]

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['birth_month'] = request.form['birth_month']
        return redirect(url_for('home'))
    return render_template("login.html")

@app.route("/home")
def home():
    if 'name' not in session:
        return redirect(url_for('login'))
    name = session['name']
    return render_template("home.html", name=name)

@app.route('/fortune')
def fortune():
    if 'name' not in session:
        return redirect(url_for('login'))

    name = session['name']
    birth_month = session['birth_month']
    if len(name) < 10:
        random_fortune = fortunes[len(name)]
    else:
        random_fortune = random.choice(fortunes)
    
    session['fortune'] = random_fortune
    return render_template("fou.html", name=name, fortune=random_fortune)

if __name__ == '__main__':
    app.run(debug=True)

