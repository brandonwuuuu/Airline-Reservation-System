from flask import Flask, render_template, request 
import sqlite3 
import sys
  
app = Flask(__name__, template_folder='system_templates') 
  
  
@app.route('/') 
@app.route('/home') 
def index(): 
    return render_template('main.html') 
  
  
connect = sqlite3.connect('airline.db')  
  
  
@app.route('/search_flight', methods=['GET', 'POST']) 
def search_flight(): 
    if request.method == 'POST': 
        connect = sqlite3.connect('airline.db') 
        destCity = request.form['destination_city'] 
        origCity = request.form['departure_city'] 
      
        cursor = connect.cursor() 
        cursor.execute('select flight_no, airline_name, dep_time, arrv_time,    orig_country, orig_city,  orig_airport, a2.country as dest_country, a2.city as dest_city, a2.airport_name as dest_airport from (select f.dest_airport_code,f.flight_no, airline_name, dep_time, arrv_time,   a.country as orig_country, a.city as orig_city,  a.airport_name as orig_airport from flight f, airport a where f.origin_airport_code=a.airport_code) temp, airport a2 where temp.dest_airport_code=a2.airport_code   and temp.orig_city=? and a2.city=?', (origCity, destCity))  
      
        data = cursor.fetchall() 
             
        return render_template("search_flight_results.html",data=data) 
   
    else: 
        return render_template('search_flight.html') 
  
  
@app.route('/tickets') 
def tickets(): 
    connect = sqlite3.connect('airline.db') 
    cursor = connect.cursor() 
    cursor.execute('select t.ticket_no, fc.flight_no, fc.class_name, fc.standard_fare,p.first_name, p.last_name from ticket t, flight_class fc, passenger p where t.flight_class_id=fc.flight_class_id and p.passenger_id = t.passenger_id and t.passenger_id=1') 
  
    data = cursor.fetchall() 
    return render_template("tickets.html", data=data) 
    
@app.route('/viewAirCraft') 
def viewAirCraft(): 
    flightNo=request.args.get('flightNo')
    print(flightNo, file=sys.stderr)
    connect = sqlite3.connect('airline.db') 
    cursor = connect.cursor() 
    cursor.execute('select at.model_no, at.manufacturer, at.aircraft_type_id from flight_aircraft fa, flight f, aircraft_type at where f.flight_no=fa.flight_no and at.aircraft_type_id=fa.aircraft_type_id and f.flight_no=?', (flightNo,))  
    data = cursor.fetchall() 
    return render_template("viewAirCraft.html", data=data)     

@app.route('/viewFlightWithAirCraft') 
def viewFlightWithAirCraft(): 
    aircraftTypeId=request.args.get('aircraftTypeId')
    print(aircraftTypeId, file=sys.stderr)
    connect = sqlite3.connect('airline.db') 
    cursor = connect.cursor() 
    cursor.execute('select flight_no from flight_aircraft where aircraft_type_id=?', (aircraftTypeId,))  
    data = cursor.fetchall() 
    return render_template("viewFlightWithAirCraft.html", data=data)     
    
@app.route('/display_flight') 
def display_flight(): 
   
    connect = sqlite3.connect('airline.db') 
    flightNo=request.args.get('flightNo')
      
    cursor = connect.cursor() 
    cursor.execute('select flight_no, airline_name, dep_time, arrv_time,    orig_country, orig_city,  orig_airport, a2.country as dest_country, a2.city as dest_city, a2.airport_name as dest_airport from (select f.dest_airport_code,f.flight_no, airline_name, dep_time, arrv_time,   a.country as orig_country, a.city as orig_city,  a.airport_name as orig_airport from flight f, airport a where f.origin_airport_code=a.airport_code) temp, airport a2 where temp.dest_airport_code=a2.airport_code   and  flight_no=?',(flightNo,))  
      
    data = cursor.fetchall() 
             
    return render_template("search_flight_results.html",data=data) 
   
  

if __name__ == '__main__': 
    app.run(debug=False) 