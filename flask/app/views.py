from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Services')
def Services():
    return render_template("Services.html")

@app.route('/Menu.html')
def Menu():
    return Menu-templates("Menu.html")


if __name__ == "__main__":
    app.run(debug=TRue)

