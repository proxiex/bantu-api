from . import db
from sqlalchemy import Column, Integer, DateTime
from datetime import datetime


class FootPrint(db.Model):
   __tablename__ = 'footprints'

   id = db.Column('id', db.Integer, primary_key = True)
   language = db.Column(db.String(250))
   platform = db.Column(db.String(250))
   user_agent = db.Column(db.String(250))
   ip_address = db.Column(db.String(250))
   latitude = db.Column(db.String(250))
   longitude = db.Column(db.String(250))
   city = db.Column(db.String(250))
   country = db.Column(db.String(250))
   time_stamp = db.Column(db.DateTime, default=datetime.now())
