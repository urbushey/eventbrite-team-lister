from flask import Flask, render_template
from simplejson import loads
import requests

app = Flask(__name__)

# eventbrite constants
EVENT_ID = '14758694653'
TOKEN = 'WO32TBATQOFVXIHTARUC'
TEAMS_API_URL = 'https://www.eventbriteapi.com/v3/events/{}/teams?token={}'

@app.route('/teams/')
def list_teams():
    r = requests.get(TEAMS_API_URL.format(EVENT_ID,TOKEN))
    teams_data = loads(r.content)
    print teams_data
    return render_template('teams.html', teams = teams_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            debug=True)
