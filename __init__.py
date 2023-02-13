from flask import Flask, render_template, request, redirect, url_for
import shelve, Feedback, Booking, Product, Inventory, Customer, User
from Forms import CreateFeedbackForm, RegisterForm, BookAppointmentForm, CreateInventoryForm, CreateCustomerForm, validators, Addproductform, UpdateAppointmentForm
from flask_bcrypt import Bcrypt

app = Flask(__name__, static_folder='static')
bcrypt = Bcrypt(app)
#Secures session cookie, Important for production environment/deployment
app.config["SECRET_KEY"] = "secretkey"

@app.route('/')
def home():
    return render_template('home.html')

## BOOKING PAGE ##

@app.route('/bookappointment', methods=['GET', 'POST'])
def book_appointment():
    book_appointment_form = BookAppointmentForm(request.form)
    if request.method == 'POST' and book_appointment_form.validate():
        bookings_dict = {}
        db = shelve.open('booking.db', 'c')
        try:
            bookings_dict = db['Bookings']
        except:
            print("Error in retrieving bookings from booking.db.")

        for key in bookings_dict:
            booking = bookings_dict.get(key)
            if (booking.get_email() == book_appointment_form.email.data):
                db.close()
                book_appointment_form.email.errors.append('A booking has already been made using this email.')
                return render_template('bookappointment.html', form=book_appointment_form)
            if (booking.get_phone() == book_appointment_form.phone.data):
                db.close()
                book_appointment_form.phone.errors.append('A booking has already been made using this phone number.')
                return render_template('bookappointment.html', form=book_appointment_form)

            if (booking.get_appdate() == book_appointment_form.appdate.data and booking.get_apptime() == book_appointment_form.apptime.data):
                db.close()
                book_appointment_form.apptime.errors.append('This time slot has already been taken.')
                return render_template('bookappointment.html', form=book_appointment_form)



        booking = Booking.Booking(book_appointment_form.name.data, book_appointment_form.email.data
                ,book_appointment_form.phone.data, book_appointment_form.appdate.data
                , book_appointment_form.apptime.data)
        bookings_dict[booking.get_booking_id()] = booking
        db['Bookings'] = bookings_dict

        db.close()

        return redirect(url_for('seebookings'))
    return render_template('bookappointment.html', form=book_appointment_form)

@app.route('/seebookings')
def seebookings():
    bookings_dict = {}
    db = shelve.open('booking.db', 'r')
    bookings_dict = db['Bookings']
    db.close()

    bookings_list = []
    for key in bookings_dict:
        booking = bookings_dict.get(key)
        bookings_list.append(booking)

    return render_template('seebookings.html',count=len(bookings_list), bookings_list=bookings_list)

@app.route('/updatebooking/<int:id>/', methods=['GET', 'POST'])
def update_booking(id):
    update_booking_form = UpdateAppointmentForm(request.form)
    if request.method == 'POST' and update_booking_form.validate():
        bookings_dict = {}
        db = shelve.open('booking.db', 'w')
        bookings_dict = db['Bookings']

        booking = bookings_dict.get(id)
        booking.set_appdate(update_booking_form.appdate.data)
        booking.set_apptime(update_booking_form.apptime.data)

        db['Bookings'] = bookings_dict
        db.close()

        return redirect(url_for('seebookings'))
    else:
        bookings_dict = {}
        db = shelve.open('booking.db', 'r')
        bookings_dict = db['Bookings']
        db.close()
        booking = bookings_dict.get(id)
        update_booking_form.appdate.data = booking.get_appdate()
        update_booking_form.apptime.data = booking.get_apptime()


        return render_template('updatebooking.html', form=update_booking_form)

@app.route('/deletebooking/<int:id>', methods=['POST'])
def delete_booking(id):
    bookings_dict = {}
    db = shelve.open('booking.db', 'w')
    bookings_dict = db['Bookings']

    bookings_dict.pop(id)

    db['Bookings'] = bookings_dict
    db.close()

    return redirect(url_for('seebookings'))

@app.route('/faq')
def faq():
    return render_template('faq.html')

## FEEDBACK PAGE ##

@app.route('/createfeedback', methods=['GET', 'POST'])
def create_feedback():
    create_feedback_form = CreateFeedbackForm(request.form)
    if request.method == 'POST' and create_feedback_form.validate():
        feedbacks_dict = {}
        db = shelve.open('feedback.db', 'c')
        try:
            feedbacks_dict = db['Feedbacks']
        except:
            print("Error in retrieving feedback from feedback.db.")

        feedback = Feedback.Feedback(create_feedback_form.name.data, create_feedback_form.remarks.data)
        feedbacks_dict[feedback.get_feedback_id()] = feedback
        db['Feedbacks'] = feedbacks_dict

        db.close()
        return redirect(url_for('home'))
    return render_template('createfeedback.html', form=create_feedback_form)

## PRODUCTS PAGE ##

@app.route('/store', methods=['GET', 'POST'])
def store():
    products_dict = {}
    db = shelve.open('product.db', 'r')
    products_dict = db['Products']
    db.close()

    products_list = []
    for key in products_dict:
        product = products_dict.get(key)
        products_list.append(product)

    return render_template('store.html', count=len(products_list), products_list=products_list)

@app.route('/addproduct', methods=['GET', 'POST'])
def add_product():
    add_product_form = Addproductform(request.form)
    if request.method == 'POST' and add_product_form.validate():
        products_dict = {}
        db = shelve.open('product.db','c')

        try:
            products_dict = db['Products']
        except:
            print("Error in retrieving products from product.db.")

        product = Product.Product(add_product_form.p_name.data, add_product_form.price.data, add_product_form.discount.data, add_product_form.stock.data, add_product_form.description.data)
        products_dict[product.get_product_id()] = product
        db['Products'] = products_dict

        db.close()

        return redirect(url_for('retrieve_products'))
    return render_template('addproduct.html', form=add_product_form)

@app.route('/retrieveProducts')
def retrieve_products():
    products_dict = {}
    db = shelve.open('product.db', 'r')
    products_dict = db['Products']
    db.close()

    products_list = []
    for key in products_dict:
        product = products_dict.get(key)
        products_list.append(product)

    return render_template('retrieveProducts.html', count=len(products_list), products_list=products_list)



@app.route('/updateproduct/<int:id>/', methods=['GET', 'POST'])
def update_product(id):
    update_product_form = Addproductform(request.form)
    if request.method == 'POST' and update_product_form.validate():
        products_dict = {}
        db = shelve.open('product.db', 'w')
        products_dict = db['Products']

        product = products_dict.get(id)
        product.set_p_name(update_product_form.p_name.data)
        product.set_price(update_product_form.price.data)
        product.set_discount(update_product_form.discount.data)
        product.set_stock(update_product_form.stock.data)
        product.set_description(update_product_form.description.data)


        db['Products'] = products_dict
        db.close()

        return redirect(url_for('retrieve_products'))
    else:
        products_dict = {}
        db = shelve.open('product.db', 'r')
        products_dict = db['Products']
        db.close()

        product = products_dict.get(id)
        update_product_form.p_name.data = product.get_p_name()
        update_product_form.price.data = product.get_price()
        update_product_form.stock.data = product.get_stock()
        update_product_form.discount.data = product.get_discount()
        update_product_form.description.data = product.get_description()


        return render_template('updateproducts.html', form=update_product_form)

@app.route('/details/<int:id>/', methods=['GET', 'POST'])
def details(id):
    products_dict = {}
    form=Addproductform(request.form)
    db = shelve.open('product.db', 'r')
    products_dict = db['Products']
    db.close()
    product = products_dict.get(id)
    product.get_p_name()
    product.get_price()
    product.get_discount()
    product.get_stock()
    product.get_description()

    return render_template('details.html', product=product)


@app.route('/deleteproduct/<int:id>', methods=['POST'])
def delete_product(id):
    products_dict = {}
    db = shelve.open('product.db', 'w')
    products_dict = db['Products']
    products_dict.pop(id)

    db['Products'] = products_dict
    db.close()

    return redirect(url_for('retrieve_products'))


## INVENTORY AND SUPPLY MGMT ##

@app.route('/createinventory', methods=['GET', 'POST'])
def create_inventory():
    create_inventory_form = CreateInventoryForm(request.form)
    if request.method == 'POST' and create_inventory_form.validate():
        inventorys_dict = {}
        db = shelve.open('inventory.db', 'c')

        try:
            inventorys_dict = db['Inventorys']
        except:
            print("Error in retrieving Inventorys from inventory.db.")

        inventory = Inventory.Inventory(create_inventory_form.area_id.data, create_inventory_form.req_stock1.data, create_inventory_form.supp_comp.data, create_inventory_form.medicine_type.data, create_inventory_form.remarks.data)
        inventorys_dict[inventory.get_inventory_id()] = inventory
        db['Inventorys'] = inventorys_dict

        db.close()

        return redirect(url_for('retrieve_inventorys'))
    return render_template('createinventory.html', form=create_inventory_form)

@app.route('/createCustomer', methods=['GET', 'POST'])
def create_customer():
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'c')

        try:
            customers_dict = db['Customers']
        except:
            print("Error in retrieving Customers from customer.db.")

        customer = Customer.Customer(create_customer_form.area_id.data, create_customer_form.req_stock1.data,
                                     create_customer_form.supp_comp.data, create_customer_form.medicine_type.data,
                                     create_customer_form.remarks.data, create_customer_form.email.data,
                                     create_customer_form.date_joined.data, create_customer_form.address.data)
##        customers_dict[customer.get_customer_id()] = customer
        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        db.close()

        return redirect(url_for('retrieve_customers'))
    return render_template('createCustomer.html', form=create_customer_form)

@app.route('/retrieveinventory')
def retrieve_inventorys():
    inventorys_dict = {}
    db = shelve.open('inventory.db', 'r')
    inventorys_dict = db['Inventorys']
    db.close()

    inventorys_list = []
    for key in inventorys_dict:
        inventory = inventorys_dict.get(key)
        inventorys_list.append(inventory)

    return render_template('retrieveinventory.html', count=len(inventorys_list), inventorys_list=inventorys_list)

@app.route('/retrieveCustomers')
def retrieve_customers():
    customers_dict = {}
    db = shelve.open('customer.db', 'r')
    customers_dict = db['Customers']
    db.close()

    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        customers_list.append(customer)

    return render_template('retrieveCustomers.html', count=len(customers_list), customers_list=customers_list)

@app.route('/updateinventory/<int:id>/', methods=['GET', 'POST'])
def update_inventory(id):
    update_inventory_form = CreateInventoryForm(request.form)
    if request.method == 'POST' and update_inventory_form.validate():
        inventorys_dict = {}
        db = shelve.open('inventory.db', 'w')
        inventorys_dict = db['Inventorys']

        inventory = inventorys_dict.get(id)
        inventory.set_area_id(update_inventory_form.area_id.data)
        inventory.set_req_stock1(update_inventory_form.req_stock1.data)
        inventory.set_supp_comp(update_inventory_form.supp_comp.data)
        inventory.set_medicine_type(update_inventory_form.medicine_type.data)
        inventory.set_remarks(update_inventory_form.remarks.data)

        db['Inventorys'] = inventorys_dict
        db.close()

        return redirect(url_for('retrieve_inventorys'))
    else:
        inventorys_dict = {}
        db = shelve.open('inventory.db', 'r')
        inventorys_dict = db['Inventorys']
        db.close()

        inventory = inventorys_dict.get(id)
        update_inventory_form.area_id.data = inventory.get_area_id()
        update_inventory_form.req_stock1.data = inventory.get_req_stock1()
        update_inventory_form.supp_comp.data = inventory.get_supp_comp()
        update_inventory_form.medicine_type.data = inventory.get_medicine_type()
        update_inventory_form.remarks.data = inventory.get_remarks()

        return render_template('updateinventory.html', form=update_inventory_form)

@app.route('/updateCustomer/<int:id>/', methods=['GET', 'POST'])
def update_customer(id):
    update_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and update_customer_form.validate():
        customers_dict = {}
        db = shelve.open('customer.db', 'w')
        customers_dict = db['Customers']

        customer = customers_dict.get(id)
        customer.set_area_id(update_customer_form.area_id.data)
        customer.set_req_stock1(update_customer_form.req_stock1.data)
        customer.set_supp_comp(update_customer_form.supp_comp.data)
        customer.set_email(update_customer_form.email.data)
        customer.set_date_joined(update_customer_form.date_joined.data)
        customer.set_address(update_customer_form.address.data)
        customer.set_medicine_type(update_customer_form.medicine_type.data)
        customer.set_remarks(update_customer_form.remarks.data)

        db['Customers'] = customers_dict
        db.close()

        return redirect(url_for('retrieve_customers'))
    else:
        customers_dict = {}
        db = shelve.open('customer.db', 'r')
        customers_dict = db['Customers']
        db.close()

        customer = customers_dict.get(id)
        update_customer_form.area_id.data = customer.get_area_id()
        update_customer_form.req_stock1.data = customer.get_req_stock1()
        update_customer_form.supp_comp.data = customer.get_supp_comp()
        update_customer_form.email.data = customer.get_email()
        update_customer_form.date_joined.data = customer.get_date_joined()
        update_customer_form.address.data = customer.get_address()
        update_customer_form.medicine_type.data = customer.get_medicine_type()
        update_customer_form.remarks.data = customer.get_remarks()

        return render_template('updateCustomer.html', form=update_customer_form)

@app.route('/deleteinventory/<int:id>', methods=['POST'])
def delete_inventory(id):
    inventorys_dict = {}
    db = shelve.open('inventory.db', 'w')
    inventorys_dict = db['Inventorys']

    inventorys_dict.pop(id)

    db['Inventorys'] = inventorys_dict
    db.close()

    return redirect(url_for('retrieve_inventorys'))

@app.route('/deleteCustomer/<int:id>', methods=['POST'])
def delete_customer(id):
    customers_dict = {}
    db = shelve.open('customer.db', 'w')
    customers_dict = db['Customers']
    customers_dict.pop(id)

    db['Customers'] = customers_dict
    db.close()

    return redirect(url_for('retrieve_customers'))

@app.route('/register', methods=['GET', 'POST'])
def register_user():
   register_form = RegisterForm(request.form)
   if request.method == 'POST' and register_form.validate():
       users_dict = {}
       db = shelve.open('Users.db', 'c')

       try:
           users_dict = db['Registered Users']
       except:
           print("Error in retrieving Registered Users from Users.db.")

       user = User.User(register_form.first_name.data, register_form.last_name.data,
                        register_form.email_add.data,register_form.username.data,register_form.gender.data,  register_form.medical.data, register_form.remarks.data, register_form.password.data, register_form.confirm_password.data)
       users_dict[user.get_user_id()] = user
       db['Registered Users'] = users_dict

       db.close()

       return redirect(url_for('retrieve_users'))
   return render_template('register.html', form=register_form)



@app.route('/retrieveUsers')
def retrieve_users():
   users_dict = {}
   db = shelve.open('Users.db', 'r')
   users_dict = db['Registered Users']
   db.close()

   users_list = []
   for key in users_dict:
       user = users_dict.get(key)
       users_list.append(user)

   return render_template('retrieveUsers.html', count=len(users_list), users_list=users_list)
#
#
#
@app.route('/updateUsers/<int:id>/', methods=['GET', 'POST'])
def update_user(id):
   update_user_form = RegisterForm(request.form)
   if request.method == 'POST' and update_user_form.validate():
       users_dict = {}
       db = shelve.open('Users.db', 'w')
       users_dict = db['Registered Users']

       user = users_dict.get(id)
       user.set_first_name(update_user_form.first_name.data)
       user.set_last_name(update_user_form.last_name.data)
       user.set_email_add(update_user_form.email_add.data)
       user.set_username(update_user_form.username.data)
       user.set_gender(update_user_form.gender.data)
       user.set_medical(update_user_form.medical.data)
       user.set_remarks(update_user_form.remarks.data)
       user.set_pwd(update_user_form.password.data)
       user.set_confirm_pwd(update_user_form.confirm_password.data)

       db['Registered Users'] = users_dict
       db.close()

       return redirect(url_for('retrieve_users'))
   else:
       users_dict = {}
       db = shelve.open('users.db', 'r')
       users_dict = db['Registered Users']
       db.close()

       user = users_dict.get(id)
       update_user_form.first_name.data = user.get_first_name()
       update_user_form.last_name.data = user.get_last_name()
       update_user_form.email_add.data = user.get_email_add()
       update_user_form.username.data = user.get_username()
       update_user_form.gender.data = user.get_gender()
       update_user_form.medical.data = user.get_medical()
       update_user_form.remarks.data = user.get_remarks()
       update_user_form.password.data = user.get_pwd()
       update_user_form.confirm_password.data = user.get_confirm_pwd()

       return render_template('updateUsers.html', form=update_user_form)

@app.route('/deleteUser/<int:id>', methods=['POST'])
def delete_user(id):
   users_dict = {}
   db = shelve.open('users.db', 'w')
   users_dict = db['Registered Users']

   users_dict.pop(id)

   db['Users'] = users_dict
   db.close()

   return redirect(url_for('retrieve_users'))

if __name__ == '__main__':
        app.run(debug=True)
