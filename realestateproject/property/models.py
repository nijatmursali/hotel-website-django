from django.db import models

# Create your models here.

PROPERTY_TYPE = (
    ('S', 'sale'),
    ('R', 'rent'),
    ('B', 'buy')
)


class Property(models.Model):
    name = models.CharField(max_length=50)
    short_description = models.CharField(max_length=100)
    long_description = models.CharField(max_length=1000)

    #condition here
    #location = models.
    type = models.CharField(choices=PROPERTY_TYPE, max_length=10)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    price  = models.PositiveIntegerField()
    area = models.DecimalField(decimal_places=2, max_digits=8)
    beds_number = models.PositiveIntegerField()
    kitchen_number = models.PositiveIntegerField()
    leavingroom_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()

    image = models.ImageField(upload_to='property')

    #amenities here

    #floor plan 
    
    #take a video tour
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
    
class Category(models.Model):
    category_name = models.CharField(max_length=30)
    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    