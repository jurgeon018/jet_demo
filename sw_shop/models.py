from django.db import models 
from mptt.models import TreeForeignKey, MPTTModel



class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(to="ItemCategory", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Item' 

    @classmethod
    def modeltranslation_fields(self):
        return ['name']

    def __str__(self):
        return f'{self.name}'

class Attribute(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

    @classmethod 
    def modeltranslation_fields(self):
        return ['name']

    class Meta:
        verbose_name = 'Attribute' 
        verbose_name_plural = 'Attribute' 
        
class AttributeValue(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.value}'

    @classmethod 
    def modeltranslation_fields(self):
        return ['value']

    class Meta:
        verbose_name = 'AttributeValue' 
        verbose_name_plural = 'AttributeValue' 


class ItemAttribute(models.Model):
    item = models.ForeignKey(to="Item", on_delete=models.CASCADE)
    attribute = models.ForeignKey(to="Attribute", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.item}:{self.attribute}'

    class Meta:
        verbose_name = 'ItemAttribute' 
        verbose_name_plural = 'ItemAttribute' 
        

class ItemAttributeValue(models.Model):
    item_attribute = models.ForeignKey(to="ItemAttribute", on_delete=models.CASCADE)
    value = models.ForeignKey(to="AttributeValue", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.item_attribute}:{self.value}'

    class Meta:
        verbose_name = 'ItemAttributeValue' 
        verbose_name_plural = 'ItemAttributeValue' 
    
class ItemFeature(models.Model):
    item    = models.ForeignKey(to="Item", on_delete=models.CASCADE)
    feature = models.ForeignKey(to="Feature", on_delete=models.CASCADE)
    value   = models.ForeignKey(to="FeatureValue", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'ItemFeature'
        verbose_name_plural = 'ItemFeature' 

    def __str__(self):
        return f'{self.feature}:{self.value}'


class Feature(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Feature'

    def __str__(self):
        return f'{self.name}'


class FeatureValue(models.Model):
    value = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'FeatureValue'
        verbose_name_plural = 'FeatureValue' 

    def __str__(self):
        return f'{self.value}'


class ItemCategory(MPTTModel):
    parent = TreeForeignKey(to='self', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    
    @classmethod
    def modeltranslation_fields(self):
        return ['name']
    
    class Meta:
        verbose_name = 'ItemCategory'
        verbose_name_plural = 'ItemCategory' 

    def __str__(self):
        return f'{self.name}'


class ItemBrand(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'ItemBrand'
        verbose_name_plural = 'ItemBrand' 

    def __str__(self):
        return f'{self.name}'


class ItemImage(models.Model):
    item = models.ForeignKey(to="Item", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'ItemImage'
        verbose_name_plural = 'ItemImage' 

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post' 

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order' 

    def __str__(self):
        return f'{self.name}'


class CartItem(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = 'CartItem'
        verbose_name_plural = 'CartItem' 

    def __str__(self):
        return f'{self.name}'



