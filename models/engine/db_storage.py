#!/usr/bin/python3
"""Define class DBStorage"""
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import MetaData, create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """Database storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes DBStorage class"""
        user = os.getenv("HBNB_MYSQL_USER")
        pswd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(user, pswd, host, db),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns dictionary of everything in database"""
        obj_list = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                obj_list[key] = obj
        else:
            for tbl in Base.__subclasses__():
                table = self.__session.query(tbl).all()
                for obj in table:
                    key = "{}.{}".format(obj.__class__.name, obj.id)
                    obj_list[key] = obj
        return obj_list

    def new(self, obj):
        """Adds new object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Saves all changes to current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes object from current database session"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """Creates new database session and loads previous objects"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Closes the current __session attribute"""
        self.__session.remove()
