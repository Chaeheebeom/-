from flask import Flask
#Flask-Migrate
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from flaskext.markdown import Markdown

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    #for database
    app.config.from_object(config)
    db.init_app(app)
    migrate.init_app(app, db)

    #for url
    from views import main_views,auth_views,comment_views,vote_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(comment_views.bp)
    app.register_blueprint(vote_views.bp)

    #필터
    from filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    #진자2에 break를 사용하기위함
    app.jinja_env.add_extension('jinja2.ext.loopcontrols')

    #마크다운
    Markdown(app,extension=['nl2br','fenced_code'])

    return app


