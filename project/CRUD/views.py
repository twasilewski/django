from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse
from CRUD.models import ItemForm
import DatabaseInteractions
from django.shortcuts import render_to_response

def index(request):
	DB = DatabaseInteractions.CRUD()
	rows = DB.getAll()
	return render(request, 'CRUD/index.html', {'rows': rows})
	
	
def item(request, item_id):

	print item_id
	DB = DatabaseInteractions.CRUD()
	item = DB.getById(item_id)
	return render(request, 'CRUD/item.html', {'item': item})

def add_item(request):
	if request.method == 'POST':
		form = ItemForm(request.POST)
		
		if form.is_valid():
			DB = DatabaseInteractions.CRUD()
			DB.create(form.instance)
			return render(request, 'CRUD/index.html')
		else:
			print form.errors
	else:
		form = ItemForm()
	return render(request, 'CRUD/add_item.html', {'form': form})

def delete(request, item_id):
	DB = DatabaseInteractions.CRUD()
	DB.deleteById(item_id)
	return render(request, 'CRUD/index.html')

def update(request, item_id):
	print "test"
	if request.method == 'POST':
		form = ItemForm(request.POST)
		
		if form.is_valid():
			DB = DatabaseInteractions.CRUD()
			form.instance.id = item_id
			DB.update(form.instance)
			return render(request, 'CRUD/index.html')
		else:
			print form.errors
	else:
		form = ItemForm()
	return render(request, 'CRUD/upgrade_item.html', {'form': form})

# Create your views here.
