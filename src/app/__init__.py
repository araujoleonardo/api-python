from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    from .routes import produto_routes
    app.register_blueprint(produto_routes.bp)
    
    with app.app_context():
        db.create_all()
    
    return app