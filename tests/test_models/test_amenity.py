#!/usr/bin/python3
"""doc"""
import pep8
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """doc"""
    obj = Amenity()

    def test_pep8(self):
        """doc"""
        pepEight = pep8.StyleGuide().check_files(['models/amenity.py'])
        self.assertEqual(pepEight.total_errors, 0)

    def test_docs(self):
        """doc"""
        self.assertIsNotNone(Amenity.__doc__)
        self.assertIsNotNone(Amenity.__init__.__doc__)
        self.assertIsNotNone(Amenity.save.__doc__)
        self.assertIsNotNone(Amenity.__str__.__doc__)
        self.assertIsNotNone(Amenity.to_dict.__doc__)

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
        self.assertIsInstance(Amenity.__dict__['name'], str)
