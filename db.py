from sqlalchemy import Column, Integer, String, create_engine, Table
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import config

engine = create_engine(config.heroku_pg)
Base = declarative_base()

class PhoneNumbers(Base):
  __tablename__ = "phone_numbers"
  id = Column(Integer, primary_key=True, autoincrement=True)
  phone_number = Column(String(20))

def add_phonenumber(phone_number):
  try:
    id = get_phonenumberid(phone_number)
    print id
    if id is None:
      num = PhoneNumbers(phone_number=phone_number)
      DBsession.add(num)
      DBsession.commit()
      return True
    return False
  except Exception as e:
    DBsession.rollback()
    return False

def get_phonenumberid(phone_number):
  try:
    q = DBsession.query(PhoneNumbers.id).filter(PhoneNumbers.phone_number
      ==phone_number).scalar()
    return q
  except Exception as e:
    DBsession.rollback()

def remove_phonenumber(phone_number):
  try:
    num = DBsession.query(PhoneNumbers).filter_by(
      phone_number=phone_number).scalar()
    DBsession.delete(num)
    DBsession.commit()
    return True
  except Exception as e:
    DBsession.rollback()
    return False

def get_allphonenumbers():
  try:
    nums = DBsession.query(PhoneNumbers.phone_number).all()
    return nums
  except Exception as e:
    DBsession.rollback()


# db inits
Base.metadata.create_all(engine)
Base.metadata.bind = engine
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
DBsession = Session()
