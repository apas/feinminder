from flask import Flask, render_template, jsonify, request, redirect
from flask.ext.basicauth import BasicAuth
import texting, config, db

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = config.auth_u
app.config['BASIC_AUTH_PASSWORD'] = config.auth_p
app.config['BASIC_AUTH_FORCE'] = True
basic_auth = BasicAuth(app)

@app.route("/")
def hello():
  try:
    subs = db.get_allphonenumbers()
  except Exception as e:
    return redirect(url_for('hello'))

  return render_template("index.html", subscribers=subs)

@app.route("/go", methods=["POST"])
def post_msg():
  msg = request.form.getlist("text_msg")
  if texting.send_text(msg):
    jsonstring = {"Message":msg[0], "Success":True}
    return jsonify(jsonstring)
  else:
    jsonstring = {"Message":msg[0], "Success":False}
    return jsonify(jsonstring)

@app.route("/sms", methods=["POST"])
def sms():
  from_number = request.values.get('From', None)
  msg_body = request.values.get('Body', None)

  if "Subscribe" in msg_body:
    try:
      return texting.subscribe(from_number)
    except Exception as e:
      resp = twilio.twiml.Response()
      resp.message("There was an error. " \
        "Please try again later.")
      return str(resp)
  elif "Unsubscribe" in msg_body:
    try:
      return texting.unsubscribe(from_number)
    except Exception as e:
      resp = twilio.twiml.Response()
      resp.message("There was an error. " \
        "Please try again later.")
      return str(resp)

if __name__ == "__main__":
  app.run(debug=True, threaded=True)
