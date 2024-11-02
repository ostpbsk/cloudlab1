# my_project/terminals/domain/terminal.py
from my_project.database import db

class Terminal(db.Model):
    __tablename__ = 'terminals'

    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255), nullable=False)
    gps_latitude = db.Column(db.Numeric(9, 6), nullable=False)
    gps_longitude = db.Column(db.Numeric(9, 6), nullable=False)
    manufacturer = db.Column(db.String(100), nullable=False)
    comissioning_date = db.Column(db.Date, nullable=False)
    customer_company_id = db.Column(db.Integer, db.ForeignKey('customer_companies.id'))

    customer_company = db.relationship("CustomerCompany", backref="terminals")

    def to_dict(self):
        return {
            "id": self.id,
            "address": self.address,
            "gps_latitude": self.gps_latitude,
            "gps_longitude": self.gps_longitude,
            "manufacturer": self.manufacturer,
            "comissioning_date": self.comissioning_date,
            "customer_company_id": self.customer_company_id,
        }
