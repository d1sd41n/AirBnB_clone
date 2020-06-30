#!/usr/bin/python3
"""doc"""
import pep8
from models.base_model import BaseModel
import unittest
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):
    """doc"""
    obj = FileStorage()
    base = BaseModel()

    def test_pep8(self):
        """doc"""
        pepEight = \
            pep8.StyleGuide().check_files(['models/engine/file_storage.py'])
        self.assertEqual(pepEight.total_errors, 0)

    def test_docs(self):
        """doc"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_class_instance(self):
        """doc"""
        dic = self.obj.all()
        self.assertEqual(type(dic), dict)
        self.base.save()
        with open('file.json', 'r') as file:
            read_j = json.loads(file.read())
        self.obj.reload()
        dic = self.obj.all()
        self.assertEqual(len(dic), len(read_j))
