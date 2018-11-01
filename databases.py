from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Write your functions to interact with the database here :

def create_product(p_type, price, quantity, description):
	new_product= Product(p_type= p_type, price= price, quantity= quantity, description= description)
	session.add(new_product)
	session.commit()

  #TODO: complete the functions (you will need to change the function's inputs)
  

def update_product(p_type, description):
  product1= session.query(Product).filter_by(p_type=p_type).first()
  product1.p_type= "hat"
  product1.description= "purple hat"
  session.commit()

  

def delete_product(id):
  session.query(Product).filter_by(id=id).delete()
  session.commit()

def get_product(id):
  pass
