# User class
class Booking:
    count_id = 0

    # initializer method
    def __init__(self,name,email,phone,appdate,apptime):
        Booking.count_id += 1
        self.__booking_id = Booking.count_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__appdate = appdate
        self.__apptime = apptime


    # accessor methods
    def get_booking_id(self):
        return self.__booking_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_appdate(self):
        return self.__appdate

    def get_apptime(self):
        return self.__apptime

    # mutator methods
    def set_booking_id(self, booking_id):
        self.__booking = booking_id

    def set_name(self, name):
        self.__name = name

    def set_email(self, email):
        self.__email = email

    def set_phone(self, phone):
        self.__phone = phone

    def set_appdate(self, appdate):
        self.__appdate = appdate

    def set_apptime(self, apptime):
        self.__apptime = apptime
