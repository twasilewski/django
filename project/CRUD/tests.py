from django.test import TestCase
import models
import sqlite3
import DatabaseInteractions

class CRUDTestCase(TestCase):
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
        self.connect()
        c = self.conn.cursor()
        c.execute("DELETE FROM Item")
        self.conn.commit()
        self.conn.close()

    def connect(self):
        self.conn = sqlite3.connect('baza.db')
    
    def test_getByIdTest(self):
        DB = DatabaseInteractions.CRUD()
        item = models.Item
        item.name = "test1"
        item.price = 1
        
        
        
        DB.create(item)
        DB.getById(0)
        # self.assertEqual("test1", item.name)







    

# Create your tests here.
