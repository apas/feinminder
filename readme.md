# feinminder

**feinminder** is a bare bones customer relationship management SMS platform built on Python, Flask, and Twilio, and deployed over Heroku.

## Installation

1. Clone this repo and `cd` in.
2. `$ virtualenv env`
3. `$ source env/bin/activate`
4. `$ pip install -r requirements.txt`

## Usage

1. Create a Twilio account and get your Twilio number, account, and token keys.
1. Enter the corresponding number and keys in `config.py`.  
    *Note: using Twilio in trial mode needs you to verify recipient's numbers first.*  
    *Note: if you add or remove recipients do not forget to change `scraping.py` accordingly.*
1. Create a free Heroku app and set it up accordingly (dyno type `web`, size `0`.)
1. Create a Heroku database instance and and enter its URI in `config.py`.
1. Push `feinminder` to Heroku.
1. In Twilio, point the POST endpoint of your Twilio phone number to the POST endpoint of your Heroku instance.

Point your customers to your Twilio number, encourage them to subscribe.

Communicate with your customers about offers, discounts, and more.

### Development and testing 

Run `feinminder` locally with `$ python app.py`, then browse `127.0.0.1:5000`.

## License

MIT
