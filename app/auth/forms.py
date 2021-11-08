from flask_wtf import FlaskForm, RecaptchaField
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, DataRequired, Length, ValidationError, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField("Username: ",
                            validators=[
                                InputRequired("You must supply a username"),
                                DataRequired("Your username must include letters and/or numbers"),
                                Length(min=6, max=20, message="Username must be between 6 and 20 characters in length.")
                            ])
    password = PasswordField("Password: ", 
                            validators=[
                                InputRequired("You need a password!"),
                                DataRequired("Your password cannot be a bunch of blank characters."),
                                Length(min=10, max=40, message="Password must be between 10 and 40 characters in length."),
                                EqualTo("password_confirm", message="Passwords do not match")
                            ])
    password_confirm = PasswordField("Confirm Password: ", 
                            validators=[
                                InputRequired("You need a password!"),
                                DataRequired("Your password cannot be a bunch of blank characters.")
                            ])
    recaptcha = RecaptchaField()
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("Username: ",
                            validators=[
                                InputRequired("You must supply a username"),
                                DataRequired("Your username must include letters and/or numbers")
                            ])
    password = PasswordField("Password: ",
                            validators=[
                                InputRequired("You must supply a password"),
                                DataRequired("The password you entered is trash."),
                                Length(min=10, max=40, message="Password must be between 10 and 40 characters in length."),
                            ])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("Login")