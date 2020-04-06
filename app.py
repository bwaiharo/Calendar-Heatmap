from flask_pymongo import PyMongo
import os
import json
import holiday_scraper
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import datetime
year = datetime.date.today().year


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or DB_URL
# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] =  os.environ.get('DATABASE_URL', '') or "mongodb://heroku_fwqfx20b:ikt9hmsrccm7c3dvcqnpebc031@ds113063.mlab.com:13063/heroku_fwqfx20b?retryWrites=false"

mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
     return render_template("index.html")

@app.route("/scrapejsonData")
def scrapejsonData():
    holiday = mongo.db.holidays
    holiday_data = holiday_scraper.scrape_holidays()
    # holiday.insert_one(holiday_data)
    holiday.update({}, holiday_data, upsert=True)

    # return jsonify(holiday_data)
@app.route('/holidayData/<country>')
@app.route("/holidayData", methods=['GET'])
def holidayData(country):
    holiday = mongo.db.holidays
    ho = [{str(year): result[country]} for result in holiday.find()]
    # ho = [result for result in holiday.find()]
    
    return jsonify(ho)

@app.route("/countryData", methods=['GET'])
def countryData():
    country = mongo.db.countries
    co = [{"Countries": result["Countries"]} for result in country.find()]
    
    
    return jsonify(co)

@app.route("/calendarData", methods=['GET'])
def calendarData():
    holiday = mongo.db.holidays
    # ca = [{"Date": result[str(year)]} for result in holiday.find()]
    ca = [result for result in holiday.find()]
    
    return jsonify(ca)
    


if __name__ == "__main__":
    app.run(debug=True)
