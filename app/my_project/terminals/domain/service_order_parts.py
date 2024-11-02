from my_project.database import db

class ServiceOrderPart(db.Model):
    __tablename__ = 'service_order_parts'

    service_order_id = db.Column(db.Integer, db.ForeignKey('service_orders.id'), primary_key=True)
    part_id = db.Column(db.Integer, db.ForeignKey('service_parts.id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "service_order_id": self.service_order_id,
            "part_id": self.part_id,
            "quantity": self.quantity
        }