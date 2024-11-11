from flask import Flask, Response

app = Flask(__name__)

@app.get("/")
def root():
    return Response("Hello World", 200)

app.run()