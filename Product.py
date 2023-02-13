# User class
class Product:
    count_id = 0

    # initializer method
    def __init__(self, p_name, price, discount, stock ,description):
        Product.count_id += 1
        self.__product_id = Product.count_id
        self.__p_name = p_name
        self.__price = price
        self.__discount = discount
        self.__description = description
        self.__stock = stock
        # self.__image=image

    # accessor methods
    def get_product_id(self):
        return self.__product_id

    def get_p_name(self):
        return self.__p_name

    def get_price(self):
        return self.__price

    def get_discount(self):
        return self.__discount

    def get_stock(self):
        return self.__stock

    def get_description(self):
        return self.__description
    #
    # def get_image(self):
    #     return self.__image

    # mutator methods


    def set_product_id(self,product_id):
        self.__product_id = product_id
    def set_p_name(self,p_name):
        self.__p_name=p_name

    def set_price(self,price):
        self.__price=price

    def set_discount(self,discount):
        self.__discount=discount

    def set_stock(self,stock):
        self.__stock = stock

    def set_description(self,description):
        self.__description = description

    # def set_image(self,image):
    #     self.__image=image
