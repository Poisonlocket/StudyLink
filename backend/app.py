from flask import Flask, Response
from blueprints.studysession_api import studysession_api

app = Flask(__name__)
# registering all blueprints
app.register_blueprint(studysession_api)


@app.get("/")
def root() -> Response:
    return Response("Hello World", 200)


app.run()
