from flask import Flask #imports the flask class from the flask module 

app = Flask(__name__) #object created by the constructor flask __name__ is a variable controlled by python that tells code what module its in """
app.config['DEBUG'] = True #Debug thing helps with displaying errors in browser and ensuring file changes while the server running (aka host swapping)"""

#decorator that creates mapping, talking about app.route line """
@app.route("/") 
def index():
    return "Hello World"

app.run()      #pass control to flask object. loops forever and never returns, so it should be put last. Carries out responsibility of servers, """
                #listening for for requests """