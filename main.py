from flask import Flask, render_template, send_from_directory
from flask_wtf import FlaskForm
from  wtforms import StringField, PasswordField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisismysecretkey'

class getInfo(FlaskForm):
    age = StringField('age')
    zipcode = StringField('zipcode')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/form", methods=['GET', 'POST'])
def form():
    form = getInfo()

    if form.validate_on_submit():
        passedage = int(form.age.data)
        passedzipcode = int(form.zipcode.data)
        print(passedage, passedzipcode)
        return '<h1>The age is {}, and the zipcode is {}.'.format(passedage, passedzipcode)
    return render_template("form.html", form = form)
@app.route('/css/<path:path>')
def css(path):
    return send_from_directory('templates/css',path)
if __name__ == "__main__":
    app.run(debug=True)