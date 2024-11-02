from my_project.database import db

class TechnicianMaintenance(db.Model):
    __tablename__ = 'technician_maintenance'

    technician_id = db.Column(db.Integer, db.ForeignKey('technicians.id'), primary_key=True, nullable=False)
    service_order_id = db.Column(db.Integer, db.ForeignKey('service_orders.id'), primary_key=True, nullable=False)
    work_duration = db.Column(db.Numeric(5, 2), nullable=False)
    cost = db.Column(db.Numeric(10, 2), nullable=False)
    

    def to_dict(self):
        return {
            "technician_id": self.technician_id,
            "service_order_id": self.service_order_id,
            "work_duration": self.work_duration,
            "cost": self.cost
        }