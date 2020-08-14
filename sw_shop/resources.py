from import_export.resources import ModelResource 
from .models import * 

class ItemResource(ModelResource):
    class Meta:
        model = Item 
        exclude = []
