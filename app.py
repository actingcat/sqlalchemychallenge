# Import the dependencies.
from flask import Flask, jsonify
import pandas as pd
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///Resources/hawaii.sqlite")
from sqlalchemy.ext.automap import automap_base
Base= automap_base() 
Base.prepare(engine, reflect=True)
Measurement=Base.classes.measurement
Station=Base.classes.station

DBSession=sessionmaker(bind=engine)
session= DBSession()

app = Flask(__name__)
@app.route('/')
def home():
    return jsonify({
        'Available Routes': [
            '/api/v1.0/precipitation',
            '/api/v1.0/stations',
            '/api/v1.0/tobs',
            '/api/v1.0/<start>',
            '/api/v1.0/<start>/<end>'
        ]
    })
        


@app.route('/api/v1.0/precipitation')
def precipitation():
    query="""
    SELECT date, prcp
    FROM measurement
    WHERE date >= date('now', '-12 months')
    """
    df = pd.read_sql(query, engine)
    prcp_dict=df.set_index('date')['prcp'].to_dict()
    return jsonify(prcp_dict)


@app.route('/api/v1.0/stations')
def stations():
    stations_list=session.query(Station.station).all()
    stations_list_json=[station[0] for station in stations_list]
    return jsonify(stations_list_json)


@app.route('/api/v1.0/tobs')
def tobs():
    most_active= session.query(Measurement.tobs).filter(Measurement.station == 'USC00519281').all()
    most_active_json=[temp[0] for temp in most_active]
    return jsonify(most_active_json)


@app.route('/api/v1.0/<start>', methods=['GET'])
def get_temp_start(start):
    results=session.query(
        func.min(Measurement.tobs),
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs)
    ).filter(Measurement.date >= start).all()

    tobs_data={
    'TMIN':results[0][0],
    'TMAX':results[0][1],
    'TAVG':results[0][2]
    }
    return jsonify(tobs_data)

@app.route('/api/v1.0/<start>/<end>', methods=['GET'])
def get_tempstartend(start, end):
    results=session.query(
        func.min(Measurement.tobs),
        func.max(Measurement.tobs),
        func.avg(Measurement.tobs)
    ).filter(Measurement.date >=start).filter(Measurement.date <=end).all()
    tobs_data={
    'TMIN':results[0][0],
    'TMAX':results[0][1],
    'TAVG':results[0][2]
    }
    return jsonify(tobs_data)
if __name__ == '__main__':
    app.run(debug=True)

