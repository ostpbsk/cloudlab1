from my_project.database import db

class ServiceOrder(db.Model):
    __tablename__ = 'service_orders'

    id = db.Column(db.Integer, primary_key=True)
    terminal_id = db.Column(db.Integer, db.ForeignKey('terminals.id'), nullable=False)
    maintenance_type_id = db.Column(db.Integer, db.ForeignKey('maintenance_types.id'), nullable=False)
    order_date = db.Column(db.Date, nullable=False)
    scheduled_date = db.Column(db.Date, nullable=False)
    total_duration = db.Column(db.Numeric(5, 2))
    total_cost = db.Column(db.Numeric(10, 2), nullable=False)

    parts = db.relationship("ServicePart", secondary="service_order_parts", backref="service_orders")
    technicians = db.relationship("Technician", secondary="technician_maintenance", backref="service_orders")

    def to_dict(self):
        return {
            "id": self.id,
            "terminal_id": self.terminal_id,
            "maintenance_type_id": self.maintenance_type_id,
            "order_date": self.order_date,
            "scheduled_date": self.scheduled_date,
            "total_duration": self.total_duration,
            "total_cost": self.total_cost
        }