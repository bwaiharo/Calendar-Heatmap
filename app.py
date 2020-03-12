from flask_pymongo import PyMongo
import os
import json
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or DB_URL
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] =  os.environ.get('DATABASE_URL', '') or "mongodb://heroku_fwqfx20b:ikt9hmsrccm7c3dvcqnpebc031@ds113063.mlab.com:13063/heroku_fwqfx20b"

mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    news = mongo.db.countries.find_one()

    return render_template("index.html", news=news)



if __name__ == "__main__":
    app.run(debug=True)
