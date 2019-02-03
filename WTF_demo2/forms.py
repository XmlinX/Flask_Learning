from wtforms import Form, StringField, IntegerField, ValidationError, BooleanField, SelectField, FileField
from wtforms.validators import Length, EqualTo, Email, InputRequired, NumberRange, Regexp, URL, UUID
#from uuid import UUID
from flask_wtf.file import file_required, file_allowed

class RegistForm(Form):
    username = StringField(validators=[Length(min=3, max=10, message="用户名长度必须在3-10位之间")])
    password = StringField(validators=[Length(min=6, max=10)])
    password_repeat = StringField(validators=[Length(min=3, max=10), EqualTo("password")])


class LoginForm(Form):
    email = StringField(validators=[Email()])
    username = StringField(validators=[InputRequired()])
    age = IntegerField(validators=[NumberRange(12, 100)])
    phone = StringField(validators=[Regexp(r'1[3587]\d{9}')])
    home_page = StringField(validators=[URL()])
    #uuid = StringField(validators=[UUID()])
    #captcha = StringField(validators=[Length(4, 4)])
    def validate_captcha(self, field):
        # print(field.data)
        if field.data != '1234':
            raise ValidationError("验证码错误")


class SettingForm(Form):
    username = StringField("用户名", validators=[InputRequired()])
    age = IntegerField("年龄", validators=[NumberRange(12, 100)])
    remember = BooleanField('记住我：')
    tags = SelectField("标签", choices=[('1','Python'),('2','Java'),('3','SQL')])


class UploadForm(Form):
    avatar = FileField(validators=[file_required(), file_allowed(['jpg', 'gif', 'png'])])
    desc = StringField(validators=[InputRequired()])