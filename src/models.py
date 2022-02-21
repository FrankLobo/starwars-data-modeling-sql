import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)


class UserFavoritesPlanets(Base):
    __tablename__ = 'userFavoritesPlanets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    planets_id = Column(Integer, ForeignKey('planets.id'))
    planets = relationship('Planets')

class UserFavoritesCharacterss(Base):
    __tablename__ = 'userFavoritesCharacterss'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    characters_id = Column(Integer, ForeignKey('characters.id'))
    characters = relationship('Characters')

class UserFavoritesVehicles(Base):
    __tablename__ = 'userFavoritesVehicles'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'))
    characters = relationship('Characters')

class UserFavoritesStarships(Base):
    __tablename__ = 'userFavoritesStarships'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    starships_id = Column(Integer, ForeignKey('starships.id'))
    starships = relationship('Starships')

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')