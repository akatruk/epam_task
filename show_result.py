path = 'scripts/increment_data_load.sql'
 
try:
    open(path, 'w').close()
except IOError:
    print('Failure')

import requests

url = "https://covidtrackerapi.bsg.ox.ac.uk/api/v2/stringency/date-range/2021-01-01/2021-08-01"
response = requests.get(url, headers={'Accept':'application/json'})
data = response.json()
data1 = data['data']['2021-01-01']

def output_api():
    k = ''
    for i in data1.items():
        k += 'INSERT INTO epam (country_code, date_value, confirmed, deaths, stringency_actual, stringency) VALUES (' + "'"+ i[1]['country_code'] + "'" + ', ' + "'"+ i[1]['date_value'] + "'" + ", " + "'"+ str(i[1]['confirmed']) + "'" + ", " + "'"+ str(i[1]['deaths']) + "'" + ", " + "'"+ str(i[1]['stringency_actual']) + "'"+ ", " + "'"+ str(i[1]['stringency']) + "'"+ '); '
    return k

with open('scripts/increment_data_load.sql', 'w') as f:
    f.write(output_api())

from flask import Flask, render_template
import authentications as au, psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import sys

app = Flask(__name__)
show_result = 'scripts/select_query.sql'
t1 = ('country_code', 'date_value', 'confirmed', 'deaths', 'stringency_actual', 'stringency')
query = 'scripts/increment_data_load.sql'

def read_file():
    with open(query, 'r') as r1:
        return r1.read()

try:
    conn = psycopg2.connect(au.connection_string)

    cur = conn.cursor()
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur.execute(read_file())

except psycopg2.DatabaseError as e:
        
    print(f'Error {e}')
    sys.exit(1)

finally:

    if conn:
        conn.close()

def read_file():
    with open(show_result, 'r') as r1:
        return r1.read()

def get_data():
    con = None

    try:
        con = psycopg2.connect(au.connection_string)


        cur = con.cursor()
        cur.execute(read_file())

        version = cur.fetchall()
        return version, False

    except psycopg2.DatabaseError as e:

        return f'Error {e}', True

    finally:

        if con:
            con.close()

@app.route('/')
def index():
    _result, _error = get_data()
    if _error:
        return render_template('output_error.html', error_fatal=_error)
    else :
        return render_template('index.html', tt1=t1, output1=_result)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=80)