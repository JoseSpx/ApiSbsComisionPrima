from flask import Flask
app = Flask(__name__)

if app.config['ENV'] == 'production':
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

from app.routes.home import home_bp  # noqa: E402
from app.routes.sbs import sbs_bp    # noqa: E402

app.register_blueprint(home_bp, url_prefix='/')
app.register_blueprint(sbs_bp, url_prefix='/sbs')




