from __future__ import unicode_literals

from django.db import models
from django import forms

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    
class ItemForm(forms.ModelForm):
    name = forms.CharField()
    price = forms.IntegerField()
    
    class Meta:
        model = Item
        exclude = ()
    
class Inventory(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
