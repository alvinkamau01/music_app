from flask_restful import Resource
from flask import request, jsonify, make_response
from models.event import Event
from utils.config import db

class EventListResource(Resource):
    def get(self):
        events = Event.query.all()
        return make_response(jsonify([event.serialize() for event in events]), 200)

    def post(self):
        data = request.get_json()
        
        # Ensure the required fields are present
        required_fields = ["name", "latitude", "longitude", "description", "price", "date", "banner_photo"]
        for field in required_fields:
            if field not in data:
                return make_response(jsonify({"error": f"{field} is required"}), 400)
        
        new_event = Event(
            name=data["name"],
            latitude=data["latitude"],
            longitude=data["longitude"],
            description=data["description"],
            price=data["price"],
            date=data["date"],
            banner_photo=data["banner_photo"],
        )

        db.session.add(new_event)
        db.session.commit()
        return make_response(jsonify(new_event.serialize()), 201)

class EventResource(Resource):
    def get(self, event_id):
        event = Event.query.get(event_id)
        if not event:
            return make_response(jsonify({"message": "Event not found"}), 404)
        return make_response(jsonify(event.serialize()), 200)
    
    def delete(self, event_id):
        event = Event.query.get(event_id)
        if not event:
            return make_response(jsonify({"message": "Event not found"}), 404)
        
        db.session.delete(event)
        db.session.commit()
        return make_response(jsonify({"message": "Event deleted"}), 200)
    
    def put(self, event_id):
        event = Event.query.get(event_id)
        if not event:
            return make_response(jsonify({"message": "Event not found"}), 404)
        
        data = request.get_json()
        event.name = data.get("name", event.name)
        event.latitude = data.get("latitude", event.latitude)
        event.longitude = data.get("longitude", event.longitude)
        event.description = data.get("description", event.description)
        event.price = data.get("price", event.price)
        event.date = data.get("date", event.date)
        event.banner_photo = data.get("banner_photo", event.banner_photo)

        db.session.commit()
        return make_response(jsonify(event.serialize()), 200)