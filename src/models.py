from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

db = SQLAlchemy()

class User(db.Model):
    # Nombre de la tabla
    __tablename__ = 'user'

    # Nombres de las columnas
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(120), unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(120))
    surname: Mapped[str] = mapped_column(String(120))
    signup_date: Mapped[str] = mapped_column(String(120))
    is_active: Mapped[bool] = mapped_column(Boolean(), nullable=False)

    favorites: Mapped[List["Favorites"]] = relationship()

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "name": self.name,
            "surname": self.surname,
            # do not serialize the password, its a security breach
        }


class Characters(db.Model):
    # Nombre de la tabla
    __tablename__ = 'characters'

    # Nombres de las columnas
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    gender: Mapped[str] = mapped_column(String(120))
    age: Mapped[str] = mapped_column(String(120))
    height: Mapped[int] = mapped_column(Integer())
    weight: Mapped[int] = mapped_column(Integer())
    
    homeplanet: Mapped[int] = mapped_column(ForeignKey("planets.id"))
    favorite: Mapped[int] = mapped_column(ForeignKey("favorites.id")) 

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
        }


class Planets(db.Model):
    # Nombre de la tabla
    __tablename__ = 'planets'

    # Nombres de las columnas
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    population: Mapped[int] = mapped_column(Integer())
    diameter: Mapped[int] = mapped_column(Integer())
    climate: Mapped[str] = mapped_column(String(120))
    terrain: Mapped[str] = mapped_column(String(120))

    native: Mapped[List["Characters"]] = relationship()
    favorite: Mapped[int] = mapped_column(ForeignKey("favorites.id"))

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "diameter": self.diameter,
            "climate": self.climate,
            "terrain": self.terrain,
        }

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Favorites(db.Model):
    # Nombre de la tabla
    __tablename__ = 'favorites'

    # Nombres de las columnas
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    user: Mapped[int] = mapped_column(ForeignKey("user.id"))
    
    character: Mapped[List["Characters"]] = relationship()
    planet: Mapped[List["Characters"]] = relationship()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }
