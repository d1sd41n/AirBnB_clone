#!/usr/bin/python3
"""Module's Doc"""
import uuid
from datetime import datetime
import models


class BaseModel:

    def __init__(self, *args, **kwargs):
        """__init__'s Doc"""
        if kwargs != {}:
            for key in kwargs:
                if key == "updated_at" or key == "created_at":
                    self.__dict__[key] = \
                        datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                    continue
                self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """__init__'s Doc"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)

    def save(self):
        """save's Doc   .isoformat()"""
        # self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns  a dict with all atributes
            of the instance"""
        dic = {}
        for key in self.__dict__:
            if key == "updated_at" or key == "created_at":
                dic[key] = str(self.__dict__[key].isoformat())
                continue
            dic[key] = self.__dict__[key]
        dic["__class__"] = type(self).__name__
        return dic
