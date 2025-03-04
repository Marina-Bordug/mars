from flask import Flask, url_for, request

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
    <img src="{url_for("static", filename="images/mars.jpeg")}"></img>
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
    <img src="{url_for("static", filename="images/mars.jpeg")}"></img>
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


@app.route("/choice/<planet_name>")
def pl_name(planet_name):
    return f'''
    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
    <h1>Моё положение: {planet_name}</h1>
    <h3>Эта планета близка к Земле;</h3>
    <div class="alert alert-success" role="alert">
                      <h3>На ней много необходимых ресурсов</h3>
                    </div>
    <div class="alert alert-secondary" role="alert">
                      <h3>На ней есть вода и атмосфера;</h3>
                    </div>
    <div class="alert alert-warning" role="alert">
                      <h3>На ней есть небольшое магнитное поле;</h3>
                    </div>
    <div class="alert alert-danger d-flex" role="alert">
                      <h3>Наконец, она просто красива!</h3>
                    </div>
'''


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def user(nickname, level, rating):
    return f'''
    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
    <h1>Результаты отбора</h1>
    <h2>Претендента на участие в миссии {nickname}</h2>
    <div class="alert alert-success" role="alert">
                      <h3>Поздравляем! Ваш рейтинг после {level} этапа отбора</h3>
                    </div>
                      <h3>составляет {rating}!</h3>
    <div class="alert alert-warning" role="alert">
                      <h3>Желаем удачи!</h3>
                    </div>
'''


@app.route("/load_photo", methods=['POST', 'GET'])
def load_p():
    if request.method == "GET":
        return f'''
        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
        <title>Отбор астронавтов</title>
        <div class="d-flex justify-content-center flex-column text-center">
            <h1>Загрузка фотографии</h1>
            <h3>для участии в миссии</h3>
        </div>'''
    elif request.method == 'POST':
        pass


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Форма для регистрации в суперсекретной системе</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">В каком вы классе</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>7</option>
                                          <option>8</option>
                                          <option>9</option>
                                          <option>10</option>
                                          <option>11</option>
                                        </select>
                                     </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8082)