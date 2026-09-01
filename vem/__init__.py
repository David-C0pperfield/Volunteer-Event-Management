#import flask - from package import class
from flask import Flask, app, render_template, session
from flask_bootstrap import Bootstrap5
from flask_mysqldb import MySQL

# database = MySQL() # create a database object, we will use this to connect to the database in our views

#create a function that creates a web application
# a web server will run this web application
def create_app():
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'BetterSecretNeeded123'

    # MYSQL configurations, use class Config from config.py, follow config_template.py for the format of config.py, config.py is in gitignore, it will not be committed to github
    app.config.from_object('vem.config.Config')

    database.init_app(app)
    
    bootstrap = Bootstrap5(app)
    
    # #importing modules here to avoid circular references, register blueprints of routes
    # from . import views
    # app.register_blueprint(views.bp)
    # from . import session

    # return app

    #importing modules here to avoid circular references, register blueprints of routes
    from . import views
    app.register_blueprint(views.bp)

    # @app.errorhandler(404) 
    # # inbuilt function which takes error as parameter 
    # def not_found(e): 
    #   return render_template("404.html"), 404


    from . import session

    return app
