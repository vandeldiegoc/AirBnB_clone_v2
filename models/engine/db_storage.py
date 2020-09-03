#!/usr/bin/python3
"""conection with database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv


class DBStorage:
    """engine conection"""
    __engine = None
    __session = None

    def __init__(self):
        """constructor"""
        my_user = getenv("HBNB_MYSQL_USER")
        my_pwd = getenv("HBNB_MYSQL_PWD")
        my_host = getenv("HBNB_MYSQL_HOST")
        my_db = getenv("HBNB_MYSQL_DB")
        my_env = getenv("HBNB_ENV")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(my_user, my_pwd, my_host,
                                              my_db), pool_pre_ping=True)
        if "test" == my_env:
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query database"""
        new_dict = {}
        objs = [v for k, v in classes.items()]
        if cls:
            if isinstance(cls, str):
                cls = classes[cls]
            objs = [cls]
        for c in objs:
            for instance in self.__session.query(c):
                key = str(instance.__class__.__name__) + "." + str(instance.id)
                new_dict[key] = instance
        return (new_dict)

    def new(self, obj):
        """add new objet in database"""
        self.__session.add(obj)

    def save(self):
        """save change"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj in database"""
        if obj:
            self.session.delete(obj)

    def reload(self):
        """make session"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(expire_on_commit=False,
                                                     bind=self.__engine))

    def close(self):
        """ call close() method on the private session attribute """
        self.__session.close()
