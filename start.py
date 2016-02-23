from flask import Flask, render_template, url_for, request
from stravalib.client import Client
from strava.objects import ActivitySet
import toolkit
import datetime
import dateutil.relativedelta

app = Flask(__name__)

@app.route('/')
def index():
	client_id = None # add id
	redirect_uri = 'http://localhost:5000/authorized'
	url = 'https://www.strava.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code' % (client_id, redirect_uri)
	return render_template('login.html', strava_login_url=url)

@app.route('/authorized', methods=['GET', 'POST'])
def authorized():
	# get access token to make requests
	client = Client()
	code = request.args.get('code')
	client.access_token = client.exchange_code_for_token(client_id=None, client_secret=None, code=code) # add id and secret

	# get data
	today = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d")
	one_month_ago = today - dateutil.relativedelta.relativedelta(months=1)
	athlete = client.get_athlete()
	activities = client.get_activities(after=one_month_ago)
	rides = toolkit.get_activity_types(activities, 'ride')
	runs = toolkit.get_activity_types(activities, 'run')
	ride_set = ActivitySet("Rides", rides)
	run_set = ActivitySet("Runs", runs)
	return render_template('main.html', athlete=athlete, activity_sets=[ride_set, run_set])

if __name__ == '__main__':
	app.run(debug=True)

url_for('static', filename='css/style.css')
url_for('static', filename='css/bootstrap.min.css')
url_for('static', filename='js/bootstrap.min.js')