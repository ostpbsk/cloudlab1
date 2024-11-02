from my_project.database import db

class MaintenanceType(db.Model):
    __tablename__ = 'maintenance_types'

    id = db.Column(db.Integer, primary_key=True)
    maintenance_type_name = db.Column(db.String(100), nullable=False)

    service_orders = db.relationship("ServiceOrder", backref="maintenance_type")
    

    def to_dict(self):
        return {
            "id": self.id,
            "maintenance_type_name": self.maintenance_type_name
        }