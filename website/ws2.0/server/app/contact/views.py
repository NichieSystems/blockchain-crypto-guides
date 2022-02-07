# from scurdex.app.auth.forms import ContactForm
from flask import render_template, make_response, current_app, flash, redirect, url_for, request
from flask_mail import Message
from flask_moment import Moment
from ..email import send_email
from config import config
import os
from .forms import ContactForm

from . import contact

@contact.route('/form', methods=['GET'])
def contact_us():
  template = render_template('contact/contact.html')
  response = make_response(template)
  response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
  return response

@contact.route('/message', methods=['GET', 'POST'])
def send_message():  
  # form = ContactForm()
  fName = request.form['fName'], lName = request.form['lName'], eAddress = request.form['eAddress'], subject=request.form['subject'], message=request.form['message']
  destination = os.environ.get('SCURDEX_ADMIN', 'scurdex@protonmail.com')
  if destination:
    send_email(destination, subject, 'contact/contact_us_email', fName=fName, lName=lName, eAddress=eAddress, subject=subject, message=message) 
    flash('Your Message Has Been Sent')
  else:
    flash('Your Message Was Not Delivered To Support Team, Please, Try Again Later')
    return redirect(url_for('contact.contact_us'))
  template = render_template('contact/email_message.html',fName=fName, lName=lName, eAddress=eAddress, subject=subject, message=message)
  response = make_response(template)
  response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
  return response

