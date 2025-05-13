from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileField
from wtforms import StringField, PasswordField, SubmitField, DateField, RadioField
from wtforms.validators import DataRequired, Email, Regexp,Length


class LoginForm(FlaskForm):
    uwa_email = StringField("Student Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Let's go!")

class RegisterForm(FlaskForm):
    register_username = StringField("Username", validators=[DataRequired()])
    register_email = StringField("Student Email", validators=[
        DataRequired(),
        Email(),
        Regexp("^[A-Za-z0-9._%+-]+@student\\.uwa\\.edu\\.au$", message="Must be a UWA student email")
    ])
    register_password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    register_birthday = DateField("Birthday", validators=[DataRequired()])
    gender = RadioField("Gender", choices=[
        ("male", "Male"),
        ("female", "Female"),
        ("other", "None-binary")
    ], validators=[DataRequired()])
    avatar = FileField("Avatar", validators=[FileAllowed(['jpg', 'jpeg', 'png'], "Images only!")])
    submit = SubmitField("Join now!")