from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, RadioField, TextField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


class LoginForm(FlaskForm):
    age = StringField('age')
    state = StringField('state')


class testing(FlaskForm):
    q11 = TextField('Playing videogames/watching TV', validators=[validators.DataRequired()])
    q12 = TextField('Hiking/Biking', validators=[validators.DataRequired()])
    
    @app.route('/quiz', methods=['GET', 'POST'])
    def home():
        form = testing(request.form)

        print(form.errors)
        if request.method == 'POST':
            print(request.form)
            q11 = request.form['Playing videogames/watching TV']
            print("", q11)
        return render_template("quiz.html")





# @app.route("/")
# def home():
#    return render_template("index.html")


# @app.route("/quiz")
# def home():
#    return render_template("quiz.html")


@app.route('/form', methods=['GET', 'POST'])
def form():
    form = LoginForm()

    if form.validate_on_submit():
        age = form.age.data
        state = form.state.data
        return redirect(url_for('home'))
    return render_template('form.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
