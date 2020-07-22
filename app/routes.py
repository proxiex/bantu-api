import json
from flask import request, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, FootPrint




@app.route('/footprints/create', methods=['POST'])
def add_footprint():
    """generate footprint."""

    data = request.get_json(force=True)

    language = data['language']
    platform = data['platform']
    user_agent = data['user_agent']
    ip_address = data['ip_address']
    latitude = data['latitude']
    longitude = data['longitude']
    city = data['city']
    country = data['country']


    new_pin = FootPrint(
        language=language,
        platform=platform,
        user_agent=user_agent,
        ip_address=ip_address,
        latitude=latitude,
        longitude=longitude,
        city=city,
        country=country
    )
    db.session.add(new_pin)  # Adds new User record to database
    db.session.commit()  # Commits all changes
    return make_response({'message': 'Footprint added sucesfully!'})


@app.route('/footprints/list', methods=['GET'])
def list_footprints():
    """list footprint"""

    db_footprint = FootPrint.query.all()
    res = []
    for d in db_footprint:
        res.append({
            "language": d.language,
            "platform": d.platform,
            "user_agent": d.user_agent,
            "ip_address": d.ip_address,
            "latitude": d.latitude,
            "longitude": d.longitude,
            "city": d.city,
            "country": d.country,
        })

    return make_response({'data': res})
