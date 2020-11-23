from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
        app = Flask(__name__)

        app.config['SECRET_KEY'] = 'dev'
        app.config['SQLALCHEMY_DATABASE_URI'] = "postgres+psycopg2://Roark:DBL11vrmt22@trading-bot.cntngi8tdvpn.us-west-2.rds.amazonaws.com:5432/Stock_Analyzer_Bot"

        db.init_app(app)

        # blueprint for auth routes in our app
        from .auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

        # Blueprint for non-auth parts of app
        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint)

        return app

