from flask import Flask, request, redirect #imports the flask class from the flask module 
import cgi
app = Flask(__name__) #object created by the constructor flask __name__ is a variable controlled by python that tells code what module its in """
app.config['DEBUG'] = True #Debug thing helps with displaying errors in browser and ensuring file changes while the server running (aka host swapping)"""

#decorator that creates mapping, talking about app.route line """
#This form is what prints out the thing on the screen i think. the /hello thing matches with line 25
#with app route
form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="post"> 
            <label for="first-name">First Name:</label>
            <input id="first-name" type="text" name="first_name" />
            <input type="submit" />
         </form>
    <body>
</html>
"""

@app.route("/") 
def index():
    return form

@app.route("/hello", methods=['POST']) #post prevents url from showing sensitive information
#you have to use a request form to use post 
def hello():
    first_name = request.form['first_name']
    return '<h1>Hello, ' + cgi.escape(first_name) + '</h1>'

#validate if time entered by user is  valid time
time_form = """
    <style>
        .error {{ color: red; }}
    </style>
    <h1>Validate Time</h1>
    <form method='POST'>
        <label>Hours (24-hour format)
            <input name="hours" type="text" value='{hours}' />
        </label>
        <p class="error">{hours_error}</p>
        <label>Minutes
            <input name="minutes" type="text" value='{minutes}' />
        </label>
        <p class="error">{minutes_error}</p>
        <input type="submit" value="Validate" />
    </form>
    """
@app.route('/validate-time')
def display_time_form():
    return time_form.format(hours='', hours_error='',
        minutes='', minutes_error='')

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route('/validate-time', methods=['POST'])
def validate_time():

    hours = request.form['hours']
    minutes = request.form['minutes']

    hours_error = ''
    minutes_error = ''

    if not is_integer(hours):
        hours_error = 'Not a valid integer'
        hours = ''
    else:
        hours = int(hours)
        if hours > 23 or hours < 0:
            hours_error = 'Hour value out of range (0-23)'
            hours = ''
    
    if not is_integer(minutes):
        minutes_error = 'Not a valid integer'
        minutes = ''
    else:
        minutes = int(minutes)
        if minutes > 59 or minutes < 0:
            minutes_error = 'Minutes value out of range (0-59)'
            minutes = ''

    if not minutes_error and not hours_error:
        time = str(hours) + ':' + str(minutes)
        return redirect('/valid-time?time={0}' .format(time))
    else:
        return time_form.format(hours_error=hours_error,
            minutes_error=minutes_error,
            hours=hours,
            minutes=minutes)


@app.route('/valid-time')
def valid_time():
    time = request.args.get('time')
    return '<h1>You submitted {0}. Thanks for submitting a valid time!</h1>' .format(time)
app.run()      #pass control to flask object. loops forever and never returns, so it should be put last. Carries out responsibility of servers, """
                #listening for for requests """