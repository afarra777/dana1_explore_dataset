"""
Main BikeShare Python File

"""
import bikeshare_lib as bs 
from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)


@app.route('/')
@app.route('/selectCity/', methods=['GET', 'POST'])
def selectCity():
    
    bs_stats = bs.BSCityStats()
    # Read the user selection
    if request.method == 'POST':
           bs_stats.selected_city = request.form['city']
           bs_stats.selected_month = request.form['month']
           bs_stats.selected_day = request.form['day']
           
    # Load and analyse Bike Share Data Based on user selections           
    bs_stats.load_data()
    bs_stats.analyse_data()
               
    return render_template('main.html', cityStats=bs_stats, messages=bs_stats.errors)
        

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)    
