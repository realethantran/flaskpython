# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
# from api import app_api # Blueprint import api definition
from bp_projects.projects import app_projects # Blueprint directory import projects definition


app.register_blueprint(app_projects) # register api routes

# @app.errorHandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/api/')
def api():
    return render_template("api.html")
    
@app.route('/mole/')  # connects /mole/ URL to mole() function
def mole():
    return render_template("mole.html")

@app.route('/my-handling-form-page')  
def form():
    return render_template("my-handling-form-page.html")


# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
