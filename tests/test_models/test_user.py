#!/usr/bin/python3
"""doc"""
import pep8
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """doc"""
    obj = User()

    def test_pep8(self):
        """doc"""
        pepEight = pep8.StyleGuide().check_files(['models/user.py'])
        self.assertEqual(pepEight.total_errors, 0)

    def test_docs(self):
        """doc"""
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)
        self.assertIsNotNone(User.save.__doc__)
        self.assertIsNotNone(User.__str__.__doc__)
        self.assertIsNotNone(User.to_dict.__doc__)

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
        self.assertIsInstance(User.__dict__['first_name'], str)
        self.assertIsInstance(User.__dict__['last_name'], str)
        self.assertIsInstance(User.__dict__['email'], str)
        self.assertIsInstance(User.__dict__['password'], str)
