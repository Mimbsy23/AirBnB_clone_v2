#!/usr/bin/python3

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from os import getenv
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.user import User
from models.base_model import Base
from models.amenity import Amenity

class DBstorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine("mysql://{}:{}@{}/{}".format(user, pwd, host, db), pool_pre_ping=True, echo=False)
        if getenv("HBNB_ENV") == "test":
            metadata = MetaData(bind=self.__engine)
            metadata.reflect()
            tables = metadata.tables
            if tables:
                for table_name in tables:
                    table = tables[table_name]
                    table.drop(self.__engine)

    def all(self, cls=None):
        all_obj_dict = {}
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if cls is not None:
            obj_dict = self.__session.query(cls).all()
            for obj in obj_dict:
                key = cls.__name__ + "." + obj.id
                obj = cls(**obj.to_dict())
                all_obj_dict.update({key: obj})
        else:
            all_class_list = [User, Review, Place, State, Amenity, City]
            for class_name in all_class_list:
                try:
                    class_obj_list = self.__session.query(class_name).all()
                    if class_obj_list:
                        for obj in class_obj_list:
                            key = class_name.__name__ + "." + obj.id
                            all_obj_dict.update({key: obj})
                except Exception as e:
                    continue
        self.__session.close()
        return all_obj_dict

    def new(self, obj):
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        self.__session.add(obj)
        
    def save(self):
        self.__session.commit()
        self.__session.close()

    def delete(self, obj=None):
        if obj is not None:
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()
            model = self.__session(type(obj)).filter(type(obj).id == obj.id).first()
            self.__session.delete(model)
            self.__session.commit()
            self.__session.close()

    def reload(self):
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
        Base.metadata.create_all(bind=self.__engine)
        self.__session.close()
