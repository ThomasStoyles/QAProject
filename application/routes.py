from cgitb import html
from flask import Flask, render_template, request, url_for, redirect
from requests import post
from application import db, app
from application.models import DevForm, Developer, Games, GameForm, DevForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, IntegerField
from flask_wtf import FlaskForm

def pop_dev(j):
    devs = db.session.query(Developer).all()
    for i in devs:
        j.developer.choices.append((i.id, i.dev_name))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods = ['GET','POST'])
def add_game():
    add = GameForm()
    pop_dev(add)
    if request.method == 'POST':
        if add.validate_on_submit():
            game = Games(
                name = add.game_name.data,
                age = int(add.age_rating.data),
                price = add.price.data,
                developer_id = add.developer.data 
                )
            db.session.add(game)
            db.session.commit()

            return redirect(url_for('read'))

    return render_template('add.html', add=add)


@app.route('/add_developer', methods = ['GET','POST'])
def add_developer():
    add_developer = DevForm()
    if request.method == 'POST':
                new_devs = Developer(dev_name=add_developer.dev_name.data)
                db.session.add(new_devs)
                db.session.commit()
                return redirect(url_for('add_developer'))

    return render_template('dev.html', add_developer=add_developer)



# prints all the games and devs in the database
@app.route('/read', methods=['GET'])
def read():
    game = Games.query.all()
    devs = Developer.query.all()
    return render_template('read.html', games=game, dev=devs)



@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    game = Games.query.get(id)
    update = GameForm()
    pop_dev(update)
        
    if request.method == 'POST':
        game.name = update.game_name.data
        game.age = int(update.age_rating.data)
        game.price = update.price.data
        game.developer_id = update.developer.data
        db.session.commit()

        return redirect(url_for('read'))

    return render_template('update.html', game=game, update=update)



@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    game = Games.query.get(id)

    db.session.delete(game)
    db.session.commit()
    return render_template ('read.html', games=Games.query.all()) 


# @app.route('/add')
# def add():
#     new_game = Games(name="New Game")
#     db.session.add(new_game)
#     db.session.commit()
#     return "Added new game to database"


# @app.route('/form', methods=['GET','POST'])
# def add_cust():
#     form = CustomerForm()

#     if request.method == 'POST':
#         if form.validsate_on_submit():
#             cust1 = CustomerForm(f_name=form.f_name.data, l_name=form.l_name.data)
#             db.seesion.add(cust1)
#             db.session.commit()

#             return f'{cust1.f_name} has been added to the database '


#     return render_template('Form.html', form=form)

    # title = task.title
    # form = taskform(title=title)





    
    # update = Games()
    # game_to_update = Games.query.get_or_404(id)
    # if request.method == 'POST':
    #     game_to_update.name = request.update['name']
    #     game_to_update.age = request.update['age']
    #     game_to_update.price = request.update['price']
    #     game_to_update.developer = request.update['developer']
    #     try:
    #         db.session.commit()
    #         print('Success')
    #         return render_template('update.html', update=update, game_to_update=game_to_update)
    #     except:
    #         db.session.commit()
    #         print('Error, Please try again')
    #         return render_template('update.html', update=update, game_to_update=game_to_update)
    # else:
    #     return render_template('update.html', update=update, game_to_update=game_to_update)