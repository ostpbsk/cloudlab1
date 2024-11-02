from my_project.database import db

class Payment(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    invoice_id = db.Column(db.Integer, db.ForeignKey('invoices.id'), nullable=False)
    payment_date = db.Column(db.Date, nullable=False)
    ammount_paid = db.Column(db.Numeric(10, 2), nullable=False)
    payment_method = db.Column(db.String(50), nullable=True)
    

    def to_dict(self):
        return {
            "id": self.id,
            "invoice_id": self.invoice_id,
            "payment_date": self.payment_date,
            "ammount_paid": self.ammount_paid,
            "payment_method": self.payment_method
        }