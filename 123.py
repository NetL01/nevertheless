from flask import Flask
from flask import render_template


app = Flask(__name__)
@app.route('/')
def one():
    return "Миссия Колонизация Марса"

@app.route('/index')
def index():
    return 'И на Марсе будут Яблони!'

@app.route('/promotion')
def promotion():
    countdown_list = ['Человечество вырастает из детства', 'Человечеству мала одна планета',
                              'Мы сделаем обитаемыми безжизненные пока планеты', 'И начнём с марса!', 'Присоединяйся!']
    countdown_list.append('Пуск!')
    return '</br>'.join(countdown_list)

@app.route('/image_mars')
def image_mars():
    return render_template('htmlcode.html')

@app.route('/promotion_image')
def image_marss():
    return render_template('promotion_image.html')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
