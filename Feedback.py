# User class
class Feedback:
    count_id = 0

    # initializer method
    def __init__(self, name, remarks):
        Feedback.count_id += 1
        self.__feedback_id = Feedback.count_id
        self.__name = name
        self.__remarks = remarks

    # accessor methods
    def get_feedback_id(self):
        return self.__feedback_id

    def get_name(self):
        return self.__name

    def get_remarks(self):
        return self.__remarks

    # mutator methods
    def set_feedback_id(self, feedback_id):
        self.__feedback_id = feedback_id

    def set_name(self, name):
        self.__name = name

    def set_remarks(self, remarks):
        self.__remarks = remarks
