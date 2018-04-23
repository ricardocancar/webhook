import json
import os
from flask import Flask, request, make_response, jsonify


app = Flask(__name__)
log = app.logger

@app.route('/')
def inicio():
  return 'hola'
@app.route('/webhook', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook
    This is meant to be used in conjunction with the weather Dialogflow agent
    """
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'

    
    res = weather(req)
    print('Action: ' + action)
    print('Response: ' + res)

    return make_response(jsonify({'fulfillmentText': res}))


def weather(req):
    """Returns a string containing text with a response to the user
    with the weather forecast or a prompt for more information
    Takes the city for the forecast and (optional) dates
    uses the template responses found in weather_responses.py as templates
    """
    parameters = req['queryResult']['parameters']

    print('Dialogflow Parameters:')
    print(json.dumps(parameters, indent=4))

    response = 'Mucho pero no te quiero decir'
    return response


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
