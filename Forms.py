from wtforms import Form, StringField, TextAreaField, validators, IntegerField, FloatField, RadioField, SelectField, PasswordField
from flask_wtf import FlaskForm
from wtforms.fields import EmailField, DateField, TimeField, FileField
from flask_wtf.file import FileAllowed,FileRequired
from wtforms.validators import InputRequired, DataRequired, Email, Length
from datetime import datetime
from flask import request
import re
import shelve



class CreateFeedbackForm(Form):
    name = StringField('Name', validators=[InputRequired()])
    reason = SelectField('Reason for feedback', choices=[('praise', 'Praise excellent service'),
                                                           ('problem', 'Report problem with medication or prescription'),
                                                           ('improvement', 'Suggest an improvement'),
                                                           ('feedback', 'Provide feedback on website or online service'),
                                                           ('complaint', 'Report complaint'),
                                                           ('other', 'Other')],
                        validators=[InputRequired()])
    remarks = TextAreaField('Remarks', validators=[InputRequired()])

class BookAppointmentForm(Form):
    def phone_number_validator(form, field):
        if len(field.data) != 8:
            raise validators.ValidationError('Phone number must be 8 digits')
        try:
            int(field.data)
        except ValueError:
            raise validators.ValidationError('Phone number must be an integer')

    def appdate_validator(form, field):
        if field.data < datetime.today().date():
            raise validators.ValidationError('Appointment date must be equal to or later than today')

    def name_validator(form, field):
        if not all(char.isalpha() or char.isspace() for char in field.data):
            raise validators.ValidationError('Name must contain only letters')

    phone = StringField('Phone Number', [validators.Length(min=1, max=150), validators.DataRequired(), phone_number_validator])
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired(), name_validator])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    appdate = DateField('Appointment Date', [validators.InputRequired(), validators.DataRequired(), appdate_validator], default=datetime.today().date(), render_kw={"min": datetime.today().date().isoformat()})
    apptime = TimeField('Appointment Time')

class UpdateAppointmentForm(Form):
    def appdate_validator(form, field):
        if field.data < datetime.today().date():
            raise validators.ValidationError('Appointment date must be equal to or later than today')
    appdate = DateField('Appointment Date', [validators.InputRequired(), validators.DataRequired(), appdate_validator], default=datetime.today().date(), render_kw={"min": datetime.today().date().isoformat()})
    apptime = TimeField('Appointment Time')

class CapitalLetterValidator(object):
    def __init__(self, message=None):
        if not message:
            message = u'First letter must be a capital letter.'
        self.message = message

    def __call__(self, form, field):
        if not re.match("^[A-Z].*", field.data):
            raise validators.ValidationError(self.message)

class PositiveIntegerValidator(object):
    def __init__(self, message=None):
        if not message:
            message = u'This field must contain a positive integer.'
        self.message = message

    def __call__(self, form, field):
        if not isinstance(field.data, float) or field.data < 0:
            raise validators.ValidationError(self.message)

class Addproductform(Form):
    p_name = StringField('Product Name',[validators.length(min=1, max=150),validators.DataRequired(),CapitalLetterValidator()])
    price=FloatField('Price',[validators.DataRequired(),PositiveIntegerValidator()])
    discount=IntegerField('Discount',default=0)
    stock=IntegerField('stock',[validators.DataRequired()])
    description=TextAreaField('Description',[validators.DataRequired()])

class CreateInventoryForm(Form):
    area_id = StringField('Area Manager ID', [validators.Length(min=1, max=150), validators.DataRequired()])
    req_stock1 = StringField('Required Stock on Medicine ', [validators.Length(min=1, max=150), validators.DataRequired()])
    supp_comp = SelectField('Supplier Companies', [validators.DataRequired()], choices=[('', 'Select'), ('A', 'ASLAN Pharmaceuticals'), ('P', 'Alliance Pharm Pte Ltd')], default='')
    medicine_type = RadioField('Type of Medicine', choices=[('P', 'Panadol'), ('T', 'Tylenol'), ('A', 'Antacids')], default='')
    remarks = TextAreaField('Remarks', [validators.Optional()])

class CreateCustomerForm(Form):
    area_id = StringField('Branch Manager ID', [validators.Length(min=1, max=150), validators.DataRequired()])
    req_stock1 = StringField('Required Amount of Medicine', [validators.Length(min=1, max=150), validators.DataRequired()])
    supp_comp = SelectField('Branch Sector', [validators.DataRequired()], choices=[('', 'Select'), ('N', 'North'), ('S', 'South')], default='')
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    date_joined = DateField('Date of Request', format='%Y-%m-%d')
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    medicine_type = RadioField('Type of medicine', choices=[('P', 'Panadol'), ('T', 'Tylenol'), ('A', 'Antacids')], default='')
    remarks = TextAreaField('Remarks', [validators.Optional()])

def validate_password(Form, field):
   if not re.search('\d', field.data):
       raise validators.ValidationError('Password must contain at least one number.')
   if not re.search('[A-Z]', field.data):
       raise validators.ValidationError('Password must contain at least a capital letter.')

class RegisterForm(Form):
    first_name = StringField('First Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    email_add = EmailField('Email Address:',[validators.Email(), validators.DataRequired(), validators.DataRequired()])
    username = StringField('Username:',[validators.Length(min=1, max=150), validators.DataRequired(), validators.DataRequired() ])
    gender = SelectField('Gender', [validators.DataRequired()],choices=[('', 'Select'), ('F', 'Female'), ('M', 'Male')], default='')
    medical = RadioField('Medical Condition', choices=[('D', 'Diabetes'), ('H', 'Heart'), ('N', 'None')], default='')
    remarks = TextAreaField('Remarks', [validators.Optional()])
    password = PasswordField('Password:',[validators.Length(min=8, max=150), validators.InputRequired(), validate_password])
    confirm_password = PasswordField('Confirm Password:',[validators.EqualTo('password', message='Passwords must match'),validators.InputRequired()])
