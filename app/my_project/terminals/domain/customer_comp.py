# my_project/customer_companies/domain/customer_comp.py
from my_project.database import db

class CustomerCompany(db.Model):
    __tablename__ = 'customer_companies'

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    contact_person = db.Column(db.String(50), nullable=False)
    contact_email = db.Column(db.String(50), nullable=False)
    contact_phone = db.Column(db.String(15), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "company_name": self.company_name,
            "contact_person": self.contact_person,
            "contact_email": self.contact_email,
            "contact_phone": self.contact_phone,
        }