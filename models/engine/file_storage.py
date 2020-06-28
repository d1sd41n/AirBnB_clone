#!/usr/bin/python3
"""Module's Doc"""
import json
import models


class FileStorage:
    __objects = {}
    __file_path = "file.json"

    # def __init__(self, *args, **kwargs):
    #     pass

    def all(self):
        return self.__objects

    def new(self, obj):
        """Adds new element to __objects"""
        name = type(obj).__name__
        self.__objects[name + "." + obj.id] = obj

    def save(self):
        dic = {}
        for key in self.__objects:
            dic[key] = self.__objects[key].to_dict()
        Json = json.dumps(dic)

        with open(self.__file_path, mode="w") as file:
            file.write(Json)

    def reload(self):
        try:
            with open(self.__file_path, mode="r") as file:
                dic = json.loads(file.read())
                for key in dic:
                    obj_name = key.split(".")[0]
                    if obj_name == "BaseModel":
                        self.__objects[key] = models.BaseModel(**dic[key])
                    elif obj_name == "User":
                        self.__objects[key] = models.User(**dic[key])

        except (FileNotFoundError, ValueError):
            self.__objects = {}
