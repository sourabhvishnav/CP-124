
from flask import Flask,jsonify,request

app = Flask(__name__)

contacts =[
    {
    'name' :' Ridhi',
    'number' : '8305820155'
   },
   {
    'name' : 'Sam',
    'number': '7412292931'
   }
        ]

@app.route("/add-data" , methods=["POST"])
def add_contact():
    if not request.json:
        return jsonify({
            "status" : "error"
        },400)
    contact= {
        'name' : request.json['name'],
         'number' : request.json['number']
    }  
    contacts.append(contact)  
    return jsonify({
        'status' : 'Added succesfully'
    })

@app.route("/get-data")    
def get_contacts():
    return jsonify({
        'data' : contacts
    })

if (__name__ == '__main__'):
    app.run(debug = True)
