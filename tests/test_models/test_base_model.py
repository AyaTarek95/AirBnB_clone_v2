#!/usr/bin/python3
""" """
from models.base_model import BaseModel, Base
import unittest
import datetime
from uuid import UUID
import json
import os
import pycodestyle
import pep8
from models import *


class test_basemodel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel


    """
    testing pep8
    """
    def test_pycodestyle(self):
        """
        Try the format
        """
        pycostyle = pycodestyle.StyleGuide(quiet=True)
        result = pycostyle.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def setUp(self):
        """ """
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ try save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)

    def test_str_method(self):
        """what STR Returns"""
        instance6 = BaseModel()
        string_output = "[BaseModel] ({}) {}".format(instance6.id,
                                                     instance6.__dict__)
        self.assertEqual(string_output, str(instance6))

    def test_uuid(self):
        """
        is unique id 4 working?
        """
        ins1 = BaseModel()
        ins2 = BaseModel()
        ins3 = BaseModel()
        insta_list = [ins1, ins2,
                          ins3]
        for insta in insta_list:
            ins_uuid = insta.id
            with self.subTest(uuid=ins_uuid):
                self.assertIs(type(ins_uuid), str)

        self.assertNotEqual(ins1.id, ins2.id)
        self.assertNotEqual(ins1.id, ins3.id)
        self.assertNotEqual(ins2.id, ins3.id)


class TestBaseModel(unittest.TestCase):
    """basem class"""

    @classmethod
    def setUpClass(cls):
        """ trying set """
        cls.base = BaseModel()
        cls.base.name = "arg"
        cls.base.num = 30

    @classmethod
    def TD(cls):
        """nah boyy"""
        del cls.base

    def TD(self):
        """TD"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_BaseModel(self):
        """Testing for pep8"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "solve it")


    def test_init_BaseModel(self):
        """try if it's work"""
        self.assertTrue(isinstance(self.base, BaseModel))

    def test_save_BaesModel(self):
        """try if it's work"""
        self.base.save()
        self.assertNotEqual(self.base.created_at, self.base.updated_at)

    def test_to_dict_BaseModel(self):
        """try if it's work"""
        base_dict = self.base.to_dict()
        self.assertEqual(self.base.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base_dict['created_at'], str)
        self.assertIsInstance(base_dict['updated_at'], str)

    def test_method_BaseModel(self):
        """any meth?"""
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        self.assertTrue(hasattr(BaseModel, "delete"))
        self.assertTrue(hasattr(BaseModel, "__init__"))

class Test_docstrings(unittest.TestCase):
    """ decorations are working """
    @classmethod
    def setup_class(self):
        """
        only for the mems
        """
        self.obj_members(BaseModel, inspect.isfunction)

if __name__ == "__main__":
    unittest.main()
