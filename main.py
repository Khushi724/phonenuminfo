from flask import Flask
app=Flask(__name__, static_url_path='/static')
@app.route('/')
def hello():
    return "Hello , this is purely made by Khushi Agarwal!"
app.run(host="0.0.0.0",port=80)
