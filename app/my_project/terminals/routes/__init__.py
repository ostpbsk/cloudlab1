# my_project/routes.py
from my_project.terminals.routes.terminal_routes import terminal_bp
from my_project.terminals.routes.customer_company_routes import customer_comp_bp
from my_project.terminals.routes.technicians_routes import technician_bp
from my_project.terminals.routes.invoices_routes import invoice_bp
from my_project.terminals.routes.maintenance_types_routes import maintenance_type_bp
from my_project.terminals.routes.service_orders_routes import service_orders_bp
from my_project.terminals.routes.payments_routes import payments_bp
from my_project.terminals.routes.service_order_parts_routes import service_order_parts_bp
from my_project.terminals.routes.service_parts_routes import service_parts_bp
from my_project.terminals.routes.technician_maintenance_routes import technician_maintenance_bp

def register_routes(app):
    app.register_blueprint(terminal_bp, url_prefix='/api')
    app.register_blueprint(customer_comp_bp, url_prefix='/api')
    app.register_blueprint(technician_bp, url_prefix='/api')
    app.register_blueprint(invoice_bp, url_prefix='/api')
    app.register_blueprint(maintenance_type_bp, url_prefix='/api')
    app.register_blueprint(service_orders_bp, url_prefix='/api')
    app.register_blueprint(payments_bp, url_prefix='/api')
    app.register_blueprint(service_order_parts_bp, url_prefix='/api')
    app.register_blueprint(service_parts_bp, url_prefix='/api')
    app.register_blueprint(technician_maintenance_bp, url_prefix='/api')
