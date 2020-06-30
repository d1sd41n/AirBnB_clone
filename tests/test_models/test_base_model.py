#!/usr/bin/python3
"""doc"""
import pep8
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """doc"""
    obj = BaseModel()

    def test_pep8(self):
        """doc"""
        pepEight = pep8.StyleGuide().check_files(['models/base_model.py'])
        self.assertEqual(pepEight.total_errors, 0)

    def test_docs(self):
        """doc"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_class_instance(self):
        """doc"""
        self.obj.name = "benito kamelas"
        self.obj.save()
        dic = self.obj.to_dict()
        self.assertEqual(dic["name"], "benito kamelas")
        self.assertEqual(type(self.obj.created_at), type(datetime.now()))
        self.assertEqual(type(self.obj.updated_at), type(datetime.now()))
        self.assertIsInstance(dic['created_at'], str)
        self.assertIsInstance(dic['updated_at'], str)
