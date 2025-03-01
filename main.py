from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return f'''

    <h1>Миссия Колонизация Марса</h1>
    '''


@app.route("/index")
def quote():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route("/promotion")
def prom():
    return '''
    <p>Человечество вырастает из детства.</p>
    <p>Человечеству мала одна планета.</p>
    <p>Мы сделаем обитаемыми безжизненные пока планеты.</p>
    <p>И начнем с Марса!</p>
    <p>Присоединяйся!</p>
    '''


@app.route("/image_mars")
def img():
    return f'''
    <title>Привет, Марс!</title>
    <h1>Жди нас, Марс!</h1>
    <img src="{url_for("static", filename="static/images/mars.jpeg")}"></img>
    '''


@app.route("/promotion_image")
def ad():
    return f'''
    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
    <link rel="stylesheet" href="statis/css/style.css">
    <title>Колонизация</title>
    <h1 class="mars-wait">Жди нас, Марс!</h1>
    <img src="{url_for("static", filename="static/images/mars.jpeg")}"></img>
    <div class="alert alert-dark" role="alert">
                      <h3>Человечество вырастет из детства.</h3>
                    </div>
    <div class="alert alert-success" role="alert">
                      <h3>Человечеству мала одна планета.</h3>
                    </div>
    <div class="alert alert-secondary" role="alert">
                      <h3>Мы сделаем обитаемыми безжизненные пока планеты.</h3>
                    </div>
    <div class="alert alert-warning" role="alert">
                      <h3>И начнём с Марса!</h3>
                    </div>
    <div class="alert alert-danger d-flex" role="alert">
                      <h3 class="pt-1 d-flex">Присоединяйся!</h3>
                    </div>
'''


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081)