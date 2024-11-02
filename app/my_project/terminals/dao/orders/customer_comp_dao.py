from my_project.terminals.dao.general_dao import GeneralDAO
from my_project.terminals.domain.customer_comp import CustomerCompany
from my_project.database import db

class CustomerCompanyDAO(GeneralDAO):
    def __init__(self):
        super().__init__(CustomerCompany)

    def get_company_terminals(self, company_id):
        company = db.session.query(CustomerCompany).filter_by(id=company_id).first()

        if company:
            terminals = [
                terminal.to_dict() for terminal in company.terminals
            ]
            return {
                "terminals": terminals
            }
        else:
            return None
