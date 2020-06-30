#!/usr/bin/python3
"""doc"""
import pep8
import unittest
from models.place import Place
from datetime import datetime


class TestUser(unittest.TestCase):
    """doc"""
    obj = Place()

    def test_pep8(self):
        """doc"""
        pepEight = pep8.StyleGuide().check_files(['models/place.py'])
        self.assertEqual(pepEight.total_errors, 0)

    def test_docs(self):
        """doc"""
        self.assertIsNotNone(Place.__doc__)
        self.assertIsNotNone(Place.__init__.__doc__)
        self.assertIsNotNone(Place.save.__doc__)
        self.assertIsNotNone(Place.__str__.__doc__)
        self.assertIsNotNone(Place.to_dict.__doc__)

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
        self.assertIsInstance(Place.__dict__['city_id'], str)
        self.assertIsInstance(Place.__dict__['user_id'], str)
        self.assertIsInstance(Place.__dict__['name'], str)
        self.assertIsInstance(Place.__dict__['description'], str)
        self.assertIsInstance(Place.__dict__['number_rooms'], int)
        self.assertIsInstance(Place.__dict__['number_bathrooms'], int)
        self.assertIsInstance(Place.__dict__['max_guest'], int)
        self.assertIsInstance(Place.__dict__['price_by_night'], int)
        self.assertIsInstance(Place.__dict__['latitude'], float)
        self.assertIsInstance(Place.__dict__['longitude'], float)
        self.assertIsInstance(Place.__dict__['amenity_ids'], list)
