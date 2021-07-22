from flask import Flask

app=Flask(__name__)

@app.route('/')

def home():
    return "homepage goes here"


@app.route('/about/')
def about():
    return "about page goes here"

if __name__ == "__main__":
    app.run(debug=True)
