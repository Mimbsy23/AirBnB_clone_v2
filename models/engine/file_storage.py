#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls == None:
            return FileStorage.__objects
        class_obj_dict = {}
        all_obj_dict = FileStorage.__objects
        class_name = cls.__name__
        all_obj_keys = all_obj_dict.keys()
        for key in all_obj_keys:
            obj_class = key.split(".")
            obj_class=obj_class[0]
            if obj_class == class_name:
                class_obj_dict.update({key: all_obj_dict[key]})
            continue
        return class_obj_dict

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete obj from __objects if it’s inside"""
        if obj is not None:
            obj_dict = self.all()
            obj_keys = obj_dict.keys()
            for key in obj_keys:
                if obj_dict[key] == obj:
                    del obj_dict[key]
                    break

