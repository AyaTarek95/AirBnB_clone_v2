#!/usr/bin/python3
""" sqlAlchemy NEW DB File """
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """ create tables in environmental"""
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
        returns a dictionary
        Return:
        returns a dictionary of __object
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
        """ add new elem to the table """
        self.__session.add(obj)

    def save(self):
        """ save the changes """
        self.__session.commit()

    def delete(self, obj=None):
        """
            delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ reload function """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
