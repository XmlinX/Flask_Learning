from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


movies = [
    {
        'id':'11212',
         'thumbnail':'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2540940050.jpg',
         'title':'印度合伙人',
         'rating':8.1,
         'comment_count':8000,
         'authors':'R·巴尔基'
     },
    {
        'id':'11213',
         'thumbnail':'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2540924496.webp',
         'title':'龙猫',
         'rating':9.3,
         'comment_count':15000,
         'authors':'宫崎骏'
     },
    {
        'id':'11343',
        'thumbnail':'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2537158013.jpg',
        'title':'毒液',
        'rating':7.3,
        'comment_count':3000,
        'authors':'鲁本·弗雷斯彻'
     }
]

tvs = [
    {
        'id':'11',
        'thumbnail':'https://img3.doubanio.com/view/subject/l/public/s28066581.jpg',
        'title':'浪潮之巅',
        'rating':9.4,
        'comment_count':10000,
        'authors':'吴军'
     },
    {
        'id':'12',
        'thumbnail':'https://img3.doubanio.com/view/subject/m/public/s8985946.jpg',
        'title':'跌荡一百年',
        'rating':8.4,
        'comment_count':13000,
        'authors':'吴晓波'
     },
    {
        'id':'13',
        'thumbnail':'https://img3.doubanio.com/view/subject/m/public/s28033891.jpg',
        'title':'转折年代',
        'rating':8.1,
        'comment_count':8000,
        'authors':'程中原'
     },
    {
        'id':'14',
        'thumbnail':'https://img1.doubanio.com/view/subject/m/public/s9085337.jpg',
        'title':'我是乔布斯',
        'rating':8.0,
        'comment_count':10000,
        'authors':'帕特丽夏'
     },
    {
        'id':'15',
        'thumbnail':'https://img1.doubanio.com/view/subject/m/public/s28024697.jpg',
        'title':'成为乔布斯',
        'rating':9.0,
        'comment_count':10000,
        'authors':'Brent Schlender'
     },
    {
        'id':'16',
        'thumbnail':'https://img1.doubanio.com/view/subject/l/public/s27653128.jpg',
        'title':'数学之美',
        'rating':9.0,
        'comment_count':1700,
        'authors':'吴军'
     }
]
@app.route('/')
def list():
    context = {
        "movies":movies,
        "tvs":tvs
    }
    return render_template('index3.html', **context)

@app.route('/list/')
def my_list():
    context = {
        "movies": movies,
        "tvs": tvs
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
