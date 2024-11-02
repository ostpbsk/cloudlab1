from my_project.database import db

class ServicePart(db.Model):
    __tablename__ = 'service_parts'

    id = db.Column(db.Integer, primary_key=True)
    part_name = db.Column(db.String(100), nullable=False)
    part_cost = db.Column(db.Numeric(10, 2), nullable=False)


    def to_dict(self):
        return {
            "id": self.id,
            "part_name": self.part_name,
            "part_cost": self.part_cost
        }