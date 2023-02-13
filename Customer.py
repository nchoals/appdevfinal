
class Customer:
    count_id = 0

    def __init__(self, area_id, req_stock1, supp_comp, medicine_type, remarks, email, date_joined, address):
        Customer.count_id += 1
        self.__customer_id = Customer.count_id
        self.__area_id = area_id
        self.__req_stock1 = req_stock1
        self.__supp_comp = supp_comp
        self.__medicine_type = medicine_type
        self.__remarks = remarks
        self.__email = email
        self.__date_joined = date_joined
        self.__address = address

    # accessor methods
    def get_inventory_id(self):
        return self.__inventory_id

    def get_area_id(self):
        return self.__area_id

    def get_req_stock1(self):
        return self.__req_stock1

    def get_supp_comp(self):
        return self.__supp_comp

    def get_medicine_type(self):
        return self.__medicine_type

    def get_remarks(self):
        return self.__remarks

    def get_customer_id(self):
        return self.__customer_id

    def get_email(self):
        return self.__email

    def get_date_joined(self):
        return self.__date_joined

    def get_address(self):
        return self.__address

    # mutator methods
    def set_inventory_id(self, inventory_id):
        self.__inventory_id = inventory_id

    def set_area_id(self, area_id):
        self.__area_id = area_id

    def set_req_stock1(self, req_stock1):
        self.__req_stock1 = req_stock1

    def set_supp_comp(self, supp_comp):
        self.__supp_comp = supp_comp

    def set_medicine_type(self, medicine_type):
        self.__medicine_type = medicine_type

    def set_remarks(self, remarks):
        self.__remarks = remarks

    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_email(self, email):
        self.__email = email

    def set_address(self, address):
        self.__address = address

    def set_date_joined(self, date_joined):
        self.__date_joined = date_joined


