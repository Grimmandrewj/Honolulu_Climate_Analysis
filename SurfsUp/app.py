# Import necessary dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# Reflect existing database into a new model.
Base = automap_base()
# Reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measure = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
# Set Homepage and list all available routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"<h1>Welcome to Climate App API!</h1><br/>"
        f"<img width='500' src='https://img.freepik.com/premium-vector/boy-surfing-man-swimming-with-body-board-big-sea-ocean-wave_104571-263.jpg?w=2000'><br/><br/>"
        f"Here are the available routes:<br/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
        f"Note: when entering dates for routes /start and /start/end, use this format: YYYY-MM-DD and YYYY-MM-DD/YYYY-MM-DD<br/>"
        f"The dataset includes data from 2016-08-23 to 2017-08-23<br/>"

    #For ease of use, include hyperlinked routes
        f"<h2>Click on the below hyperlinks to be directed to each route:</h2>"
        f"<ol><li><a href=http://127.0.0.1:5000/api/v1.0/precipitation>"
        f"List of precipitation totals by date for most recent 12 months of data</a></li><br/>"
        f"<li><a href=http://127.0.0.1:5000/api/v1.0/stations>"
        f"List of weather station locations and station IDs</a></li><br/>"
        f"<li><a href=http://127.0.0.1:5000//api/v1.0/tobs>"
        f"List of last 12 months of temp measurements for most active station (USC00519281)</a></li><br/>"
        f"<li><a href=http://127.0.0.1:5000/api/v1.0/2016-08-23>"
        f"After entering start date (YYYY-MM-DD), displays average, minimum, and maximum temps for all dates equal to or greater than date entered</a></li><br/>"
        f"<li><a href=http://127.0.0.1:5000/api/v1.0/2016-08-23/2017-08-23>"
        f"After entering a start and end date (YYYY-MM-DD/YYYY-MM-DD), displays average, minimum, and maximum temps for dates between start and end date (inclusive of end date)</a></li></ol><br/>"
    )

    

# Create route to display 12 month precipitation data
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create a session (link) from Python to the database
    session = Session(engine)

    # Run query to find last 12 months of precipitation data
    year_precip = session.query(Measure.date, Measure.prcp)\
        .filter(Measure.date >= '2016-08-23')\
        .order_by(Measure.date).all()
    
    # Convert results to dictionary with date as key and prcp as value
    prcp_dict = dict(year_precip)

    # Creturn json list of dictonary
    return jsonify(prcp_dict)

    # Close session
    session.close()

# Create route to display list of stations in the dataset
@app.route("/api/v1.0/stations")
def stations():
    # Create a session (link) from Python to the database
    session = Session(engine)

    # Run query to obtain all station info
    stations = session.query(Station.name, Station.station).all()

    # Convert results to a dictionary
    stations_dict = dict(stations)

    # Return dictionary of stations (name and station number)
    return jsonify(stations_dict)

    # Close session
    session.close()

# Create route for 12 months of dates and temp observations for most active station
@app.route("/api/v1.0/tobs")
def tobs():
    # Create a session (link) from Python to the database
    session = Session(engine)

    # Query 12 months of date and temp data for most active station
    tobs_station = session.query(Measure.date, Measure.tobs)\
        .filter(Measure.date >= '2016-08-23')\
        .filter(Measure.station == "USC00519281")\
        .order_by(Measure.date).all()
    
    # Convert results to dict to show date and temp info
    tobs_dict = dict(tobs_station)

    # Return json version of dictionary
    return jsonify(tobs_dict)

    # Close session
    session.close()

# Create route to return min, max, and average temp from start date
@app.route("/api/v1.0/<start>")
def start_date(start):
    # Create a session (link) from Python to the database
    session = Session(engine)

    # Create query for min, max, and average tobs for dates >= user submission
    start_date_results = session.query(func.min(Measure.tobs), func.max(Measure.tobs), func.avg(Measure.tobs))\
        .filter(Measure.date >= start).all()
    
    # Close session
    session.close()

    # Create list of min, max, and avg temps to populate dictionary with query results
    start_date_values = []
    for min, max, avg in start_date_results:
        start_date_dict = {}
        start_date_dict["min"] = min
        start_date_dict["max"] = max
        start_date_dict["average"] = avg
        start_date_values.append(start_date_dict)

    # Return json version of dictionary
    return jsonify(start_date_values)

# Create route to return min, max, and avg temps with start and end date
@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    # Create a session (link) from Python to the database
    session = Session(engine)

    # Run query for min, max, and avg temps for dates = start date and <= user submission (end date)
    start_end_date_results = session.query(func.min(Measure.tobs), func.max(Measure.tobs), func.avg(Measure.tobs))\
        .filter(Measure.date >= start)\
        .filter(Measure.date <= end).all()
    
    # Close session
    session.close()

    # Create list of min, max, and average temps to append dictionary values
    start_end_date_values = []
    for min, max, avg in start_end_date_results:
        start_end_date_dict = {}
        start_end_date_dict["min_temp"] = min
        start_end_date_dict["max_temp"] = max
        start_end_date_dict["avg_temp"] = avg
        start_end_date_values.append(start_end_date_dict)

    # Return json version of dictionary
    return jsonify(start_end_date_values)

if __name__ == '__main__':
    app.run(debug=True)





        

