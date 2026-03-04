from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


class LoginForm(FlaskForm):
    email = StringField(label='Email')
    password = PasswordField(label='Password')
    submit = SubmitField(label='Login')

app.secret_key = "any-string-you-want-just-keep-it-secret"
bootstrap = Bootstrap5(app)

@app.route("/login",methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    print(login_form.email.data)
    return render_template('login_before.html', form=login_form)


class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
Email=StringField('Email',validators=[DataRequired(),Email(allow_empty_local=True,message="Invalid Email Address"),Length(min=4)])


if __name__ == '__main__':
    app.run(debug=True,port=8080)
