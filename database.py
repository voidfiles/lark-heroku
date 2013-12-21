import os
import re

from flask import Flask
from flask_cors import CrossOriginResourceSharing

from lark.ext.flask.redis_api import redis_api_blueprint
from lark.ext.flask.flask_redis import Redis

app = Flask(__name__)
app.config.from_object(__name__)
app.config['REDIS_URL'] = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
app.config['DEFAULT_LARK_SCOPES'] = set(['admin'])


allowed = (
    re.compile("^.*$"),  # Match a regex
)

cors = CrossOriginResourceSharing(app)
cors.set_allowed_origins(*allowed)
Redis(app)
app.register_blueprint(redis_api_blueprint, url_prefix='/api/0')


@app.route("/")
def helloWorld():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)
