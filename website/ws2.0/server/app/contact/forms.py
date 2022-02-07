from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from wtforms.widgets.core import TextArea
from ..models import User

class ContactForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    phonenumber= StringField('Phone Number', validators=[DataRequired()])
    subject= StringField('Message Subject', validators=[DataRequired()])
    message= TextAreaField('Tell us about your question', validators=[DataRequired()])
    email_message = BooleanField('Email', validators=[DataRequired()])
    phone_message = BooleanField('Phone', validators=[DataRequired()])
    submit = SubmitField('Submit Form')