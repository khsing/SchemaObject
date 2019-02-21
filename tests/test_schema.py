#!/usr/bin/python
import unittest
import schemaobject

from . import TEST_DATABASE_URL

class TestSchema(unittest.TestCase):

    def setUp(self):
        self.database_url = TEST_DATABASE_URL
        self.db = schemaobject.SchemaObject(self.database_url + 'sakila', charset='utf8mb4')
        self.db2 = schemaobject.SchemaObject(self.database_url, charset='utf8mb4')

    def test_database_version(self):
        assert self.db.version == "5.6.21"

    def test_port(self):
        assert self.db.port == 3306

    def test_host(self):
        assert self.db.host == "localhost"

    def test_user(self):
        assert self.db.user == "test_sakila"

    def test_selected_databse(self):
        assert self.db.selected.name == "sakila"

    def test_no_selected_databse(self):
        assert self.db2.selected == None

    def test_database_count_with_selected_databse(self):
        assert len(self.db.databases) == 1
