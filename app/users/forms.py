from flask_wtf import Form
from wtforms import TextField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = TextField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

class ChangePassword(Form):
    oldpass = PasswordField('oldpass', validators=[DataRequired()])
    newpass1 = PasswordField('newpass1', validators=[DataRequired()])
    newpass2 = PasswordField('newpass2', validators=[DataRequired()])

class AddUser(Form):
    username = TextField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    admin = BooleanField('admin')

class ModifyUser(Form):
    username = TextField('username', validators=[DataRequired()])
    password = PasswordField('password')
    admin = BooleanField('admin')
