from django.contrib import admin 
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline, TranslationTabularInline
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin, TreeRelatedFieldListFilter
from nested_admin import NestedTabularInline, NestedStackedInline, NestedModelAdmin
from .models import *

class ItemImageInline(
    NestedTabularInline,
    ):
    extra = 0
    # classes = ['collapse']
    exclude = []
    model = ItemImage


class ItemFeatureInline(
    NestedTabularInline,
    ):
    extra = 0
    # classes = ['collapse']
    exclude = []
    model = ItemFeature

class ItemAttributeValueInline(
    NestedTabularInline,
    ):
    extra = 0
    # classes = ['collapse']
    exclude = []
    model = ItemAttributeValue


class ItemAttributeInline(
    NestedTabularInline,
    admin.StackedInline,
    ):
    extra = 0
    # classes = ['collapse']
    exclude = []
    model = ItemAttribute
    inlines = [
        ItemAttributeValueInline
    ]


from .resources import * 
@admin.register(Item)
class ItemAdmin(
    TabbedTranslationAdmin,
    NestedModelAdmin,
    ImportExportModelAdmin,
    ImportExportActionModelAdmin,
    admin.ModelAdmin,
    ):
    resource_class = ItemResource
    list_filter = [
        'category',
    ]
    inlines = [
        ItemImageInline,
        ItemFeatureInline,
        ItemAttributeInline,
    ]

@admin.register(Attribute)
class AttributeAdmin(
    # TabbedTranslationAdmin,
    admin.ModelAdmin,
    ):
    pass 

@admin.register(AttributeValue)
class AttributeValueAdmin(
    TabbedTranslationAdmin,
    ):
    pass 

@admin.register(ItemAttribute)
class ItemAttributeAdmin(
    admin.ModelAdmin,
    ):
    pass 

@admin.register(ItemAttributeValue)
class ItemAttributeValueAdmin(
    admin.ModelAdmin,
    ):
    pass 

@admin.register(ItemFeature)
class ItemFeatureAdmin(
    admin.ModelAdmin,
    ):
    pass 

@admin.register(Feature)
class FeatureAdmin(
    admin.ModelAdmin,
    ):
    pass 

@admin.register(FeatureValue)
class FeatureValueAdmin(
    admin.ModelAdmin,
    ):
    pass 

@admin.register(ItemCategory)
class ItemCategoryAdmin(
    admin.ModelAdmin,
    ):
    pass 

@admin.register(ItemBrand)
class ItemBrandAdmin(
    admin.ModelAdmin,
    ):
    pass 

@admin.register(ItemImage)
class ItemImageAdmin(
    admin.ModelAdmin,
    ):
    pass 

@admin.register(Post)
class PostAdmin(
    admin.ModelAdmin,
    ):
    pass 

@admin.register(Order)
class OrderAdmin(
    admin.ModelAdmin,
    ):
    pass 

@admin.register(CartItem)
class CartItemAdmin(
    admin.ModelAdmin,
    ):
    pass 
