# User class
class User:
   count_id = 0

   # initializer method
   # Details needed are Email_add, username, Fname, lname, pwd, confirm pwd, gender)
   def __init__(self, first_name, last_name, email_add, username,gender, medical, remarks, pwd, confirm_password):
       User.count_id += 1
       self.__user_id = User.count_id
       self.__first_name = first_name
       self.__last_name = last_name
       self.__email_add = email_add
       self.__username = username
       self.__gender = gender
       self.__medical = medical
       self.__remarks = remarks
       self.__password = pwd
       self.__confirm_password = confirm_password


   # accessor methods
   def get_user_id(self):
       return self.__user_id

   def get_first_name(self):
       return self.__first_name

   def get_last_name(self):
       return self.__last_name

   def get_email_add(self):
       return self.__email_add

   def get_username(self):
       return self.__username

   def get_gender(self):
       return self.__gender

   def get_medical(self):
       return self.__medical

   def get_remarks(self):
       return self.__remarks

   def get_pwd(self):
       return self.__password

   def get_confirm_pwd(self):
       return self.__confirm_password

   # mutator methods
   def set_user_id(self, user_id):
       self.__user_id = user_id

   def set_first_name(self, first_name):
       self.__first_name = first_name

   def set_last_name(self, last_name):
       self.__last_name = last_name

   def set_email_add(self, email_add):
       self.__email_add = email_add

   def set_username(self, username):
       self.__username = username

   def set_gender(self, gender):
       self.__gender = gender

   def set_medical(self, medical):
       self.__medical = medical

   def set_remarks(self, remarks):
       self.__remarks = remarks

   def set_pwd(self, password):
       self.__password = password

   def set_confirm_pwd(self, confirm_password):
       self.__confirm_password = confirm_password
