from flask import request, jsonify
from config import app, db
from models import Contact

#decorator
@app.route("/contacts", methods=["GET"])
def get_contacts():
    #uses sqlalchemy to get all of the different contexts that exist inside of the db
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"contacts": json_contacts})

if __name__ == "__main__":
    #checks if we have a db present, if not its created
    with app.app_context():
        db.create_all()
# this runs our code, to spin up all our endpoints and apis 
    app.run(debug=True)    

