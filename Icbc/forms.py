from wtforms import Form, StringField, FloatField
from wtforms.validators import Email, Length, EqualTo, InputRequired



class RegistForm(Form):
    email = StringField(validators=[Email()])
    username = StringField(validators=[Length(3,20)])
    password = StringField(validators=[Length(6,20)])
    password_repeat = StringField(validators=[EqualTo('password')])
    deposit = FloatField(validators=[InputRequired()])
