# User class
class Inventory:
    count_id = 0

    # initializer method
    def __init__(self, area_id, req_stock1, supp_comp, medicine_type, remarks):
        Inventory.count_id += 1
        self.__inventory_id = Inventory.count_id
        self.__area_id = area_id
        self.__req_stock1 = req_stock1
        self.__supp_comp = supp_comp
        self.__medicine_type = medicine_type
        self.__remarks = remarks

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
