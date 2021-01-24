from flask import Flask, request, render_template
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

list_of_softwares = [{
    'Name': 'Python',
    'Author': 'Guido Van Rossum',
    'Version': '3.9.1',
    'Year': 2020,
    'Price': 50
}, {
    'Name': 'C',
    'Author': 'Dennis Ritchie',
    'Version': 'C17',
    'Year': 2018,
    'Price': 45
}, {
    'Name': 'C++',
    'Author': 'Bjarne Stroustrap',
    'Version': 'C++20',
    'Year': 2020,
    'Price': 45
}, {
    'Name': 'JavaScript',
    'Author': 'Brenden Eich',
    'Version': 'ECMAScript',
    'Year': 2020,
    'Price': 50
}, {
    'Name': 'Java',
    'Author': 'James Gosling',
    'Version': '15.0.1',
    'Year': 2020,
    'Price': 30
}, {
    'Name': 'R',
    'Author': 'Ross and Robert',
    'Version': '4.0.3',
    'Year': 2020,
    'Price': 40
}, {
    'Name': 'Kotlin',
    'Author': 'JetBrains',
    'Version': '1.4.0',
    'Year': 2020,
    'Price': 40
}, {
    'Name': 'PHP',
    'Author': 'Rasmus Lerdorf',
    'Version': '8.0.1',
    'Year': 2021,
    'Price': 35
}, {
    'Name': 'Go',
    'Author': 'Dennis Ritchie',
    'Version': '1.15.7',
    'Year': 2021,
    'Price': 35
}, {
    'Name': 'Scala',
    'Author': 'Guido Van Rossum',
    'Version': '2.13.4',
    'Year': 2019,
    'Price': 30
}]


@app.route('/')
def onRender():
    return json.dumps(list_of_softwares)


@app.route('/filter', methods=['POST'])
def filtering():
    receiveData = json.loads(request.data)
    returnValue = []

    if receiveData["author"] != '' and receiveData["year"] != '':
        for software in list_of_softwares:
            if software["Author"] == receiveData["author"] and software["Year"] == int(receiveData["year"]):
                returnValue.append(software)
    elif receiveData["author"] != '':
        for software in list_of_softwares:
            if software["Author"] == receiveData["author"]:
                returnValue.append(software)
    else:
        for software in list_of_softwares:
            if software["Year"] == int(receiveData["year"]):
                returnValue.append(software)
    return json.dumps(returnValue)


@app.route('/sort', methods=['POST'])
def sorting():
    receiveData = json.loads(request.data)
    returnValue = []

    if receiveData["field"] == 1:
        returnValue = sorted(receiveData["price"], key=lambda k: k['Price'])
        return json.dumps(returnValue)
    else:
        firstSort = sorted(receiveData["price"], key=lambda k: k['Year'])
        returnValue = sorted(firstSort, key=lambda k: k['Author'])
        return json.dumps(returnValue)


if __name__ == "__main__":
    app.run()
