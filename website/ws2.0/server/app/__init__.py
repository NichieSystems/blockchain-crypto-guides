from flask import Flask
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment
from flask_pagedown import PageDown
from flask_migrate import Migrate, upgrade
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
migrate = Migrate()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)   
    pagedown.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)

    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        sslify = SSLify(app)


    # Registering subpackages of the Scurdex projects with Blueprint for factory instances creation

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    from .tokenofferings import tokenofferings as tokenofferings_blueprint
    app.register_blueprint(tokenofferings_blueprint, url_prefix='/tokenofferings')   

    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint, url_prefix='/blog')

    from .contact import contact as contact_blueprint
    app.register_blueprint(contact_blueprint, url_prefix='/contact')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth') 

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='api')

    return app
