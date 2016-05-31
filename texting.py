import config
from twilio.rest import TwilioRestClient
import twilio.twiml
import db

account = config.twilio_account
token = config.twilio_token
client = TwilioRestClient(account, token)

def generator():
  try:
    customers = db.get_allphonenumbers()
  except Exception as e:
    print e
    raise Exception("Database i/o error")
  for customer in customers:
    yield customer

def send_with_twilio(customer, text_msg):
  try:
    message = client.messages.create(
              to=customer,
              from_=config.from_twilio,
              body=text_msg)
    return True
  except Exception as e:
    print e
    return False

def send_text(text_msg):
  try:
    g = generator()
    for i in g:
      send_with_twilio(i, text_msg)
    return True
  except Exception as e:
    print e
    return False

def subscribe(phone_number):
  print db.add_phonenumber(phone_number)
  resp = twilio.twiml.Response()
  resp.message("You've subscribed successfully. " \
    "Text 'Unsubscribe' for the messages to stop.")
  return str(resp)

def unsubscribe(phone_number):
  print db.remove_phonenumber(phone_number)
  resp = twilio.twiml.Response()
  resp.message("You've unsubscribed successfully.")
  return str(resp)
