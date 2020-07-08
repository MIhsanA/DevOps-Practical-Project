from flask import Flask, Response, request
import requests

app = Flask(__name__)

@app.route('/colour', methods=['POST'])
def colour():
    car= request.data2.decode('utf-8')
    person = request.data.decode('utf-8')

    if person[0].lower() in "red":
        color = f"red {car}"
        return Response(colour, mimetype='text/plain')

    elif person[0].lower() in "grey":
        color = f"greyc {car}"
        return Response(colour, mimetype='text/plain')
    
    elif person[0].lower() in "white":
        color = f"white {car}"
        return Response(colour, mimetype='text/plain')

    elif person[0].lower() in "blue":
        color = f"blue {car}"
        return Response(colour, mimetype='text/plain')

    elif person[0].lower() in "green":
        color = f"green {car}"
        return Response(colour, mimetype='text/plain')

    else:
        color = f"black {car}"
        return Response(colour, mimetype='text/plain')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5003)
