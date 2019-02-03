from flask import Flask, request, render_template, send_from_directory
from forms import RegistForm, LoginForm, SettingForm, UploadForm
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict


app = Flask(__name__)
UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'images')

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login/', methods=['GET', 'POST'])
def Login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return "Success"
        else:
            print(form.errors)
            return "Fail"


@app.route('/setting/', methods=['GET', 'POST'])
def Setting():
    if request.method == "GET":
        form = SettingForm()
        return render_template('settings.html', form=form)


@app.route('/upload/', methods=['GET', 'POST'])
def Upload():
    if request.method == "GET":
        return render_template("upload_file.html")
    else:
        form = UploadForm(CombinedMultiDict([request.form, request.files]))
        if form.validate():
            desc = request.form.get('desc')#获取描述信息
            avatar = request.files.get('avatar')
            filename = secure_filename(avatar.filename)
            avatar.save(os.path.join(UPLOAD_PATH, filename))
            print(desc)
            return "文件上传成功"
        else:
            print(form.errors)
            return "Failed"




if __name__ == '__main__':
    app.run(debug=True)
