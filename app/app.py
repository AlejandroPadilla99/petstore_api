from flask import Flask
from routes.user_routes import user_router
from routes.item_routes import item_router

app = Flask(__name__)

app.register_blueprint(user_router)
app.register_blueprint(item_router)

if __name__ == "main":
    app.run(host="127.0.0.1")