from django.db import models

class Product(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название продукта'
    )
    description = models.TextField(
        verbose_name='Описание продукта'
    )
    category = models.CharField(
        max_length=255,
        verbose_name='Категория продукта'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена продукта'
    )
    delivery = models.BooleanField(
        default=False,
        verbose_name='Доставка'
    )
    image = models.ImageField(
        upload_to='products/',
        verbose_name='Главное изображение'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title']

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Фото {self.product.title}"

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total(self):
        return self.product.price * self.quantity
