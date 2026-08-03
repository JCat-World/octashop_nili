from django.db import models
from treebeard.mp_tree import MP_Node
from django.utils.translation import gettext_lazy as _

from apps.catalogs.managers import CategoryManager

from libs.db.fields import UpperCaseCharField



class Category(MP_Node):
    title = models.CharField(_("title"), max_length=255 , db_index=True)
    description = models.CharField(_("description"), max_length=2048, null=True, blank=True)
    is_public = models.BooleanField(_("is public"), default=True)
    slug = models.SlugField(_("slug"), max_length=255, unique=True, db_index=True, allow_unicode=True)
    
    objects = CategoryManager()
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
        
    def __str__(self):
        return self.title
    
    

class OptionGroup(models.Model):
    title = models.CharField(_("title"), max_length=255 , db_index=True)

    class Meta:
        verbose_name = 'option group'
        verbose_name_plural = 'option groups'
        
        
    def __str__(self):
        return self.title
    
    
    
class OptionGroupValue(models.Model):
    title = models.CharField(_("title"), max_length=255 , db_index=True)
    group = models.ForeignKey(OptionGroup, on_delete=models.CASCADE, related_name='values', verbose_name=_("group"))

    class Meta:
        verbose_name = 'option group value'
        verbose_name_plural = 'option group values'
        
        
    def __str__(self):
        return self.title
    
class ProductClass(models.Model):
    title = models.CharField(_("title"), max_length=255 , db_index=True)
    description = models.CharField(_("description"), max_length=2048, null=True, blank=True)
    slug = models.SlugField(_("slug"), max_length=255, unique=True, db_index=True, allow_unicode=True)
    
    track_stock = models.BooleanField(_("track stock"), default=True)
    require_shipping = models.BooleanField(_("require shipping"), default=True)
    
    options = models.ManyToManyField('Option', related_name='product_classes', verbose_name=_("options"), blank=True)

    class Meta:
        verbose_name = 'product class'
        verbose_name_plural = 'product classes'
        
        
    def __str__(self):
        return self.title
    
    @property
    def has_attributes(self):
        return self.products_attributes.exists()

class ProductAttribute(models.Model):
    
    class AttributeTypeChoice(models.TextChoices):
        TEXT = 'text', _("Text")
        BOOLEAN = 'boolean', _("Boolean")
        INTEGER = 'integer', _("Integer")
        FLOAT = 'float', _("Float")
        DATE = 'date', _("Date")
        DATETIME = 'datetime', _("DateTime")
        OPTION_GROUP = 'option_group', _("Option Group")
        OPTION = 'option', _("Option")
        MULTI_OPTION = 'multi_option', _("Multi Option")
        
        
    title = models.CharField(_("title"), max_length=255 , db_index=True)
    product_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE, related_name='products_attributes', verbose_name=_("product class"), null=True)
    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, related_name='attributes', verbose_name=_("option group"), null=True, blank=True)
    type = models.CharField(_("type"), max_length=20, choices=AttributeTypeChoice.choices, default=AttributeTypeChoice.TEXT)
    required = models.BooleanField(_("required"), default=False)
    
    
    class Meta:
        verbose_name = 'product attribute'
        verbose_name_plural = 'product attributes'
        
        
    def __str__(self):
        return self.title
    
    
    

class Option(models.Model):
    
    class OptionTypeChoice(models.TextChoices):
        TEXT = 'text', _("Text")
        BOOLEAN = 'boolean', _("Boolean")
        INTEGER = 'integer', _("Integer")
        FLOAT = 'float', _("Float")
        DATE = 'date', _("Date")
        DATETIME = 'datetime', _("DateTime")
        OPTION_GROUP = 'option_group', _("Option Group")
        OPTION = 'option', _("Option")
        MULTI_OPTION = 'multi_option', _("Multi Option")
        
        
    title = models.CharField(_("title"), max_length=255 , db_index=True)
    option_group = models.ForeignKey(OptionGroup, on_delete=models.PROTECT, related_name='option_attributes', verbose_name=_("option group"), null=True, blank=True)
    type = models.CharField(_("type"), max_length=20, choices=OptionTypeChoice.choices, default=OptionTypeChoice.TEXT)
    required = models.BooleanField(_("required"), default=False)
    
    
    class Meta:
        verbose_name = 'Option'
        verbose_name_plural = 'Options'
        
        
    def __str__(self):
        return self.title
    
    
class Product(models.Model):
    class ProductTypeChoice(models.TextChoices):
        standalone = 'standalone', _("Standalone")
        parent = 'parent', _("Parent")
        child = 'child', _("Child")
    
    structure = models.CharField(_("structure"), max_length=20, choices=ProductTypeChoice.choices, default=ProductTypeChoice.standalone)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', verbose_name=_("parent"), null=True, blank=True)
    is_public = models.BooleanField(_("is public"), default=True)
    title = models.CharField(_("title"), max_length=255 , db_index=True)
    upc = UpperCaseCharField(_("upc"), max_length=12, null=True, blank=True, unique=True)
    description = models.CharField(_("description"), max_length=2048, null=True, blank=True)
    slug = models.SlugField(_("slug"), max_length=255, unique=True, db_index=True, allow_unicode=True)
    meta_title = models.CharField(_("meta title"), max_length=255, null=True, blank=True)
    meta_description = models.TextField(_("meta description"), null=True, blank=True)
    meta_keywords = models.CharField(_("meta keywords"), max_length=1024, null=True, blank=True)
    product_class = models.ForeignKey(ProductClass, on_delete=models.PROTECT, related_name='products', verbose_name=_("product class"))
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name=_("category"))
    
    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
        
    def __str__(self):
        return self.title