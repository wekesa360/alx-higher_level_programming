#!/usr/bin/python3
"""
Contains the FileStorage class
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}

class FileStorage:
    """ serializes instances to a JSON file and deserializes back to instances"""

    # string - path to JSON file
    __file_path = "file.json"
    # dictionary - emoty but will store all objects by <class name>.id
    __objects = {}

    def all (self, cls=None):
        """Returns the dictionary __objects"""
        if cls is not None:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.__name__:
                    new_dict[key] = value
            return new_dict
        return self.__objects

    def save(self):
        """serializes __objects to the JSON file (path:__file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                json_file = json.load(f)
            for key in json_file:
                self.__objects[key] = classes[json_file[key]["__class__"]](**json_file[key])
        except:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it's inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '+' + obj.id

        if key in self.__objects:
            del self.__objects[key]

    def close(self):
        """ Call reload() method for deserializing the JSON file to objects """
        self.reload()