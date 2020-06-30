#!/usr/bin/python3
"""Module's Doc"""
import json
import models


class FileStorage:
    """doc"""
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """doc"""
        return self.__objects

    def new(self, obj):
        """Adds new element to __objects"""
        name = type(obj).__name__
        self.__objects[name + "." + obj.id] = obj

    def save(self):
        """doc"""
        dic = {}
        for key in self.__objects:
            dic[key] = self.__objects[key].to_dict()
        Json = json.dumps(dic)

        with open(self.__file_path, mode="w") as file:
            file.write(Json)

    def reload(self):
        """doc"""
        try:
            with open(self.__file_path, mode="r") as file:
                dic = json.loads(file.read())
                for key in dic:
                    obj_name = key.split(".")[0]

                    self.__objects[key] = \
                        models.dic_classes[obj_name](**dic[key])

        except (FileNotFoundError, ValueError):
            self.__objects = {}
