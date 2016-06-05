from django.test import TestCase
import models
import sqlite3
import DatabaseInteractions

class CRUDTestCase(TestCase):
    def clean(self):
        self.connect()
        c = self.conn.cursor()
        c.execute("DELETE FROM Item")
        self.conn.commit()
        self.conn.close()
        
    def setUp(self):
        self.connect()
        c = self.conn.cursor()
        c.execute("DELETE FROM Item")
        
        item = models.Item
        item.name = "test1"
        item.price = 1
        
        c.execute('INSERT INTO Item (Name, Price) VALUES(?, ?)',
                            (item.name, item.price)
                        )
                        
        self.conn.commit()
        self.conn.close()
        
    def tearDown(self):
        self.clean()

    def connect(self):
        self.conn = sqlite3.connect('baza.db')
    
    def test_getByIdTest(self):
        DB = DatabaseInteractions.CRUD()
        item = models.Item
        item.name = "test1"
        item.price = 1

        id = DB.create(item)
        item2 = DB.getById(id)
        self.assertEqual(item2.name, item.name)

    def test_create(self):
        self.clean()
        
    
        DB = DatabaseInteractions.CRUD()
        item = models.Item
        item.name = "test1"
        item.price = 1
        
        id = DB.create(item)
        item2 = DB.getById(id)
        self.assertEqual(item2.name, item.name)

    def test_update(self):
        self.clean()
        DB = DatabaseInteractions.CRUD()
        item = models.Item
        item.name = "test1"
        item.price = 1
        
        id = DB.create(item)
        
        item.id = id
        
        item.name = "update1"
        
        DB.update(item)
        item2 = DB.getById(item.id)
        
        
        self.assertEqual(item2.name, "update1")
        
    def test_delete(self):
        self.clean()
        DB = DatabaseInteractions.CRUD()
        item = models.Item
        item.name = "test1"
        item.price = 1
        
        id = DB.create(item)
        item2 = DB.getById(id)
        DB.deleteById(item2.id)
        item2 = DB.getById(id)
    

    

# Create your tests here.
