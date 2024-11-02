from my_project.database import db

class Invoice(db.Model):
    __tablename__ = 'invoices'

    id = db.Column(db.Integer, primary_key=True)
    service_order_id = db.Column(db.Integer, db.ForeignKey('service_orders.id'), nullable=False)
    invoice_date = db.Column(db.Date, nullable=False)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    payment_status = db.Column(db.String(50), nullable=False)

    payments = db.relationship("Payment", backref="invoice")

    def to_dict(self):
        return {
            "id": self.id,
            "service_order_id": self.service_order_id,
            "invoice_date": self.invoice_date,
            "total_amount": self.total_amount,
            "payment_status": self.payment_status
        }