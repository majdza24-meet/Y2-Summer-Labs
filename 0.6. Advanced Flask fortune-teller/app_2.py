from flask import Flask, render_template
import random

app = Flask(__name__ , template_folder= "templates")

@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/fortune')
def fortune():
    fortune_list=["Luck seemed to follow her like a shadow","Sometimes, all you need is a little luck to change your fortunes.","With a stroke of luck, we found the missing keys.","Every roll of the dice seems to go my way.","I feel blessed to have such fortunate circumstances.","Somehow, against all odds, everything turned out perfectly.","The lucky charm I carry always brings me good fortune."," I stumbled upon a lucky penny just when I needed it most.","Finding a four-leaf clover made my day!"," Luck is what happens when preparation meets opportunity."]
    random_fortune=fortune_list[random.randint(0,2)]
    return render_template("fou.html",f=random_fortune)

if __name__ == '__main__':
    app.run(debug=True, port = 5001)

