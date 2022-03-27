from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(80))
  last_name = db.Column(db.String(80))
  phone_number = db.Column(db.String(80))
  email_address = db.Column(db.String(80))
  pin_number = db.Column(db.String(80))
  county = db.Column(db.String(80))
  city = db.Column(db.String(80))
  state = db.Column(db.String(80))
  zip_code = db.Column(db.String(80))

  def to_dict(self):
    return {
      "id":self.id,
      "first_name": self.first_name,
      "last_name": self.last_name,
      "phone_number": self.phone_number,
      "email_address": self.email_address,
      "pin_number":  self.pin_number,
      "county": self.county,
      "city": self.city,
      "state": self.state,
      "zip_code": self.zip_code
    }