from flask import Flask, Response, request
import requests

app = Flask(__name__)

@app.route('/colour', methods=['POST'])
def colour():

    person = request.data.decode('utf-8')

    if person[0].lower() in "red":
        colour = "red"
        return Response(colour, mimetype='text/plain')

    elif person[0].lower() in "gray":
        colour = "gray"
        return Response(colour, mimetype='text/plain')
    
    elif person[0].lower() in "white":
        colour = "white"
        return Response(colour, mimetype='text/plain')

    elif person[0].lower() in "blue":
        colour = "blue"
        return Response(colour, mimetype='text/plain')

    elif person[0].lower() in "green":
        colour = "green"
        return Response(colour, mimetype='text/plain')

    else:
        colour = "black"
        return Response(colour, mimetype='text/plain')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)
