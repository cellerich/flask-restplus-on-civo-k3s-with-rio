from flask import Flask
from app.apis import api

app = Flask(__name__)

api.init_app(app)
app.config["RESTPLUS_MASK_SWAGGER"] = False


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(debug=True)
