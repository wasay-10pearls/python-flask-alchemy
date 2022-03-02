from crypt import methods
from flask import Flask, jsonify, request


app = Flask(__name__)

stores = [
    {
        "items": [
            {
                "id": 1,
                "name": "pepsi"
            }
        ],
        "name": "beverage"
    }
]

@app.route('/')
def home():
    return "Hello, World"

@app.route('/store', methods= ['POST'])
def create_store():
    request_data= request.get_json()
    new_store= {'name': request_data['name'], 'items':[]}
    stores.append(new_store)
    return jsonify({'stores':stores})

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        else:
            return jsonify({'error':'no store'})

@app.route('/store')
def get_all_stores():
    return jsonify({"store": stores})

@app.route('/store/<string:name>/item',  methods=['POST'])
def create_item_in_store(name):
    request_data= request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item= {'id': request_data['id'], 'name':request_data['name']}
            store['items'].append(new_item)
            return jsonify(new_item)
        return({'error': 'no store found'})


@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
        else:
            return jsonify({'error': 'no store found'})

app.run(port=5000)












