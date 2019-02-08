from flask import Flask, render_template, views, request
from forms import RegistForm
from exts import db
import config
from flask_wtf import CSRFProtect


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
CSRFProtect(app)


@app.route('/')
def index():
    return render_template('index.html')


class RegistView(views.MethodView):

    def get(self):
        return render_template('regist.html')

    def post(self):
        form = RegistForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            deposit = form.deposit.data
        else:
            print(form.errors)
            return "注册失败"

app.add_url_rule('/regist/', view_func=RegistView.as_view('regist'))



if __name__ == '__main__':
    app.run()
