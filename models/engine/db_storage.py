#!/usr/bin/python3
""" sqlalchemy database """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from os import getenv
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ Define dbstorage class"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns all objects
        """
        if cls is None:
            all_objects = []
            for model_class in [User, State, City, Amenity, Place, Review]:
                all_objects.extend(self.__session.query(model_class).all())
        else:
            all_objects = self.__session.query(cls).all()

        result_dict = {"{}.{}".format(type(obj).__name__, obj.id):
                       obj for obj in all_objects}
        return result_dict

    def new(self, obj):
        """ define add method  """
        self.__session.add(obj)

    def save(self):
        """ defines save method """
        self.__session.commit()

    def delete(self, obj=None):
        """
            defines delete method
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Defines reload method """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
