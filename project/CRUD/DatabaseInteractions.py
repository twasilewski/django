import sqlite3
import sys
import models
class CRUD():

    def connect(self):
        self.conn = sqlite3.connect('baza.db')
   
    def update(self, item):
        self.connect()
        c = self.conn.cursor()
        
        c.execute('UPDATE Item SET name = ?, price = ? WHERE id = ?', (item.name, item.price, item.id))
        self.conn.commit()
        self.conn.close()

    def create(self, item):
        self.connect()
        c = self.conn.cursor()
        # try:
        #     c.execute('CREATE TABLE Item(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INT)')
        # except Exception as e:
        #     print e
            
        c.execute('INSERT INTO Item (Name, Price) VALUES(?, ?)',
                        (item.name, item.price)
                    )
        self.conn.commit()
        id = c.lastrowid
        
        
        
            
        self.conn.close()
        return id
            
    def getAll(self):
        self.connect()
        c = self.conn.cursor()    
        c.execute('SELECT * FROM Item')
        rows = c.fetchall()
        self.conn.close()
        
        
        items_list = []
        for row in rows:
            item = models.Item()
            item.id = row[0]
            item.name = row[1]
            item.price = row[2]
            items_list.append(item)
        
        return items_list
    
    def getById(self, id):
        self.connect()
        c = self.conn.cursor()
        c.execute('SELECT * FROM Item WHERE Id = ?', (id,))
        
        
        row = c.fetchone()
        item = models.Item()
        
        
        
        item.id = row[0]
        item.name = row[1]
        item.price = row[2]
        
        
        return item
    def deleteById(self, id):
        self.connect()
        c = self.conn.cursor()
        c.execute('DELETE FROM Item WHERE Id = ?', (id,) )
        self.conn.commit()
        self.conn.close()
        
            