from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory

from .models import (Option,
                     ProductClass,
                     Category, ProductAttribute, ProductRecommendation, Product, ProductAttributeValue)


class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)


admin.site.register(Category, CategoryAdmin)

admin.site.register(Option)


class AttributeCountFilter(admin.SimpleListFilter):
    title = 'attribute count'
    parameter_name = 'attribute_count'

    def lookups(self, request, model_admin):
        return (
            ('0', 'No attributes'),
            ('1', 'Has attributes'),
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(products_attributes__isnull=True)
        elif self.value() == '1':
            return queryset.filter(products_attributes__isnull=False)
        return queryset


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 1


class ProductRecommendationInline(admin.TabularInline):
    model = ProductRecommendation
    extra = 1
    fk_name = 'primary'  # Specify the foreign key field to use for the inline


@admin.register(ProductClass)
class ProductClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'track_stock',
                    'require_shipping', 'has_attributes')
    list_filter = ('track_stock', 'require_shipping', AttributeCountFilter)
    prepopulated_fields = {'slug': ('title',)}
    # Add the inline for product attributes and recommendations
    inlines = [ProductAttributeInline]
    actions = []


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug',)
    inlines = [
        # ProductAttributeValueInline,
        ProductRecommendationInline]
    prepopulated_fields = {"slug": ("title",)}