from typing import Optional
import firebase_admin
from firebase_admin import auth
from firebase_admin.auth import TokenSignError, UserNotFoundError, UserRecord
from firebase_admin import credentials, firestore
from firebase_admin.exceptions import FirebaseError, ResourceExhaustedError
from flask import Flask, abort, request, jsonify, render_template, make_response, send_from_directory, url_for
import flask
import os, time, json, requests
from werkzeug.sansio.response import Response

# Initialize Flask App Engine
app = Flask(__name__, static_url_path='', template_folder='templates')

def format_server_time():
  server_time = time.localtime()
  return time.strftime("%I:%M:%S %p", server_time)

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/', methods=['GET'])
def index():
  context = { 'server_time': format_server_time() }
  # 1
  template = render_template('index.html', context=context)
  # 2
  response = make_response(template)
  # 3
  response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
  return response

@app.route('/blog', methods=['GET'])
def blog():
  template = render_template('blog.html')
  response = make_response(template)
  response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
  return response

@app.route('/blog/<int:post_id>', methods=['GET'])
def blog_post(post_id):
  #id = request.args.get(post_id, type=int)
  filename = 'post'+str(post_id)+'.html'
  template = render_template(filename, post_id=post_id)
  response = make_response(template)
  response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
  return response

@app.route('/contact', methods=['GET'])
def contact():
  template = render_template('contact.html')
  response = make_response(template)
  response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
  return response

@app.route('/message', methods=['GET', 'POST'])
def send_message():
  template = render_template('email_message.html',fName=request.form['fName'], lName=request.form['lName'], eAddress=request.form['eAddress'])
  response = make_response(template)
  response.headers['Cache-Control'] = 'public, max-age=300, s-maxage=600'
  return response



"""
# Initialize Firebase DB by Using a service account

cred = credentials.Certificate("curdex-firebase-adminsdk-7c0y3-8509da7b89.json")
firebase_admin.initialize_app(cred)

# Initialize on Google Cloud Platform - Use the application default credentials
# cred = credentials.ApplicationDefault()
# firebase_admin.initialize_app(cred, {
# 'projectId': 'curdex',
# })

db = firestore.client()
col_ref = db.collection(u'users')

# new_user: UserRecord
FIREBASE_WEB_API_KEY = os.environ.get("AIzaSyBR3FrA3pPg5R3TExyJ3hMFG1sBOlZBPTY")
SEND_EMAIL_ENDPOINT = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode"



def create_newuser(email_id: str, pwd: str, name: str, sub: Optional[str]) -> UserRecord:
  return auth.create_user(email=email_id, password=pwd, display_name=name, subscribe = sub) if sub else auth.create_user(email=email_id, password=pwd, display_name=name)
   

def send_email_verification_link(user_token: str):
  payload = json.dumps({"requestType": "VERIFY_EMAIL", "idToken": user_token})
  res = requests.post(SEND_EMAIL_ENDPOINT, params={"key": FIREBASE_WEB_API_KEY}, data=payload)
  return res.json()

def send_password_reset_email(user_token: str):
  payload = json.dumps({"requestType": "PASSWORD_RESET", "idToken": user_token})
  res = requests.post(SEND_EMAIL_ENDPOINT, params={"key": FIREBASE_WEB_API_KEY}, data=payload)
  return res.json()


@app.route('/api/users/signup', methods=['POST'])
def register():

  # Extract the required data from the request body of the client
  if request.method == 'POST':
    try:
       email_id = request.form.get('email', type=str)
       pwd = request.form.get('password',type=str)
       pwd_confirm = request.form.get('password_confirmation', type=str)
       display_name = request.form.get('display_name', type=str)
       subscribe = request.form.get('subscription', type=bool)
    except ValueError as e:
      return abort(404, 'Error encountered extracting data from FormURLEncoded')


  # Create a new user with data received from the client and proceed to verify email  
  if (auth.get_user_by_email(email_id) == None) and (pwd == pwd_confirm):            
    
    try:
      new_user: UserRecord = create_newuser(email_id, pwd, display_name, subscribe)
      new_user_token = auth.create_custom_token(new_user.uid) 
      send_email_verification_link(new_user_token)
    except FirebaseError as e:
      abort(Response("User Record Not Found"))
    except TokenSignError:
      abort(404)

    response = jsonify({
                    "email": email_id, 
                    "password": pwd, 
                    "password_confirmation": pwd_confirm,
                    "display_name": display_name,
                    "subscription": subscribe 
                  })
    response.status_code = 201
    return response

  else:
    return jsonify({"result": "User Registration Failure"})


@app.route('/api/users/reset_password', methods=['POST']) 
def reset_password():
  if request.method == 'POST':  
    email_id = request.form.get("email")  

    try:      
      verified_email: UserRecord = auth.get_user_by_email(email_id)
      send_password_reset_email(verified_email.email)
    except UserNotFoundError:
      abort(404)
    except FirebaseError:
      abort(404)
    except ValueError:
      abort(404)

  # return jsonify({"email": result.email})

@app.route('/api/users/login', methods=['POST'])
def login():
  pass   

"""

if __name__ == '__main__':
   app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))