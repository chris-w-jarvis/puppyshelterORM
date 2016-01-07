# define our orm intial connection, creates a file called puppies
from sqlalchemy import create_engine
engine = create_engine('sqlite:///puppies.db')

# import our base class that we use to make orm classes
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# import the sql structures to build our first class
from sqlalchemy import Column, Integer, String

# declaring relationships: import foreign key concept
# the primary_key option is a parameter of Column, defaults to false
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# build shelter class, these classes all inherit from the declarative_base
class Shelters(Base):
	__tablename__ = 'shelters'

	# we need name, address, city, state, zip, website, id (pk)
	name = Column(String)
	address = Column(String)
	city = Column(String)
	state = Column(String)
	zipCode = Column(String)
	website = Column(String)
	id = integer(id, primary_key=True)

	# declare the relationship to puppies
	puppies = relationship('Puppies', back_populates = 'shelters')

# build puppy class
class Puppies(Base):
	__tablename__ = 'puppies'

	# we need name, dob, gender, weight, shelter_id
	name = Column(String)
	dob = Column(Integer)
	gender = Column(String)
	weight = Column(Integer)
	shelter_id = Column(Integer, ForeignKey('shelters.id'))

	# declare a relationship with Shelters class, check docs on this
	shelters = relationship("Shelters", back_populates = 'puppies')
	# the back_populates makes the relationship work in reverse too
