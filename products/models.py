from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Name of Category')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Product(models.Model):
    title = models.CharField(
        max_length=200,
        unique= True,
        verbose_name = 'Name of Article'
    )
    description = models.TextField(verbose_name='Enter a Description')
    image = models.ImageField(upload_to='Products/', verbose_name='Photos')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated at')
    view = models.IntegerField(default=0, verbose_name='Views')
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Price')
    is_published = models.BooleanField(default=True, verbose_name='Is Published')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
