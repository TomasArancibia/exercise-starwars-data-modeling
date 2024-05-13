import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Game(Base):
    __tablename__ = 'Game'
    id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False, unique=True)
    Region = Column(String, nullable=False)
    ReleaseDate = Column(String, nullable=False)

class Character(Base):
    __tablename__ = 'Character'
    id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=False)
    Job = Column(String, nullable=False)
    Gender = Column(String, nullable=False)
    Game = Column(Integer, ForeignKey('Game.id'))

class Pokemon(Base):
    __tablename__ = 'Pokemon'
    id = Column(Integer, primary_key=True)
    Name = Column(String(12), nullable=False)
    Types = Column(String, nullable=False)
    Gender = Column(String, nullable=False)
    FirstGame = Column(Integer, ForeignKey('Game.id'))
    BST = Column(Integer)
    Shiny = Column(Boolean)

class Favorites(Base):
    __tablename__ = 'Favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    FavoritePokemon = Column(Integer, ForeignKey('Pokemon.id'))
    FavoriteGame = Column(Integer, ForeignKey('Game.id'))
    FavoriteCharacter = Column(Integer, ForeignKey('Character.id'))

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    Name = Column(String(12), nullable=False)
    Lastname = Column(String(12), nullable=False)
    Username = Column(String(12), nullable=False, unique =True)
    Email = Column(String(12), nullable=False, unique =True)
    Age = Column(Integer)
    Favorties = Column(Integer, ForeignKey('Favorites.id'))

## Draw from SQLAlchemy base
Game.Professor = Column(Integer, ForeignKey('Character.id'))
render_er(Base, 'diagram.png')
