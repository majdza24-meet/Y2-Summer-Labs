from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__,template_folder="templates")

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        birth_month = request.form['birthmonth']
        return redirect(url_for('fortune', month=birth_month))

@app.route('/fortune/<month>')
def fortune(month):
    fortune_list=["Success is a journey, not a destination.","You will receive unexpected money.","Good things come to those who wait.","","","","","",""]
    index=len(month)
    if index>0 and index<=9:
        return render_template("fortune.html",f=fortune_list[index-1])
    else:
        return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)