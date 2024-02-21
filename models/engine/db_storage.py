from os import environ
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
""" import the necessary modules and classes"""

user = environ.get('HBNB_MYSQL_USER')
password = environ.get('HBNB_MYSQL_PWD')
host = environ.get('HBNB_MYSQL_HOST', 'localhost')
database = environ.get('HBNB_MYSQL_DB')


class DBStorage:
    """class defination"""
    __engine = None
    __session = None

    def __init__(self):
        """initializes the DBStorage object"""
        user = environ.get("HBNB_MYSQL_USER")
        password = environ.get("HBNB_MYSQL_PWD")
        host = environ.get("HBNB_MYSQL_HOST", "localhost")
        db = environ.get("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.
            format(user, password, host, db),
            pool_pre_ping=True)

        if environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ returns a dictionary containing all objects \
                of a given class, or all objects if no class is specified"""
        classes = [User, State, City, Amenity, Place, Review]
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        objects = {}
        if cls is not None and cls in classes:
            classes = self.__session.query(cls).all()
        else:
            classes = []
            for cls in [User, State, City, Amenity, Place, Review]:
                classes.extend(self.__session.query(cls).all())

        for obj in classes:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            objects[key] = obj
        self.__session.close()
        return objects

    def new(self, obj):
        """adds an object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes made to the current\
                database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes an object from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """recreates the database session and creates\
                all the tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def close(self):
        """closing current db seesion"""
        self.__session.close()
