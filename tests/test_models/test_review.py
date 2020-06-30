#!/usr/bin/python3
"""doc"""
import pep8
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """doc"""
    obj = Review()

    def test_pep8(self):
        """doc"""
        pepEight = pep8.StyleGuide().check_files(['models/review.py'])
        self.assertEqual(pepEight.total_errors, 0)

    def test_docs(self):
        """doc"""
        self.assertIsNotNone(Review.__doc__)
        self.assertIsNotNone(Review.__init__.__doc__)
        self.assertIsNotNone(Review.save.__doc__)
        self.assertIsNotNone(Review.__str__.__doc__)
        self.assertIsNotNone(Review.to_dict.__doc__)

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
        self.assertIsInstance(Review.__dict__['place_id'], str)
        self.assertIsInstance(Review.__dict__['user_id'], str)
        self.assertIsInstance(Review.__dict__['text'], str)
