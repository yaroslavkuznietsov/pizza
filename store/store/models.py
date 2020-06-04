from django.db import models


class Ingredient(models.Model):
    """
    Ingredient model.
    """
    name = models.CharField(max_length=64)
    # pizza_set -> [Pizza1, Pizza2, ...]

    def __str__(self):
        return self.name


class Size:
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'

    SIZE_OPTIONS = (
        (SMALL, 'Small'),
        (MEDIUM, 'Medium'),
        (LARGE, 'Large'),
    )


class Pizza(models.Model):
    """
    Pizza model.
    """

    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient)
    # size = models.CharField(max_length=1, choices=Size.SIZE_OPTIONS, default=Size.MEDIUM)
    price_small = models.DecimalField(max_digits=4, decimal_places=2)
    price_medium = models.DecimalField(max_digits=4, decimal_places=2)
    price_large = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.title} : {', '.join([ingr.name for ingr in self.ingredients.all()])}"


class Order(models.Model):
    """
    Order model.
    """
    address = models.CharField(max_length=64)
    phone = models.CharField(max_length=15)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Order #{self.id}'

    @property
    def total_price(self):
        return sum([item.total_price for item in self.items.all()])


class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    size = models.CharField(max_length=1, choices=Size.SIZE_OPTIONS)

    @property
    def total_price(self):
        pizza_price_size_mapping = {
            Size.SMALL: self.pizza.price_small * self.quantity,
            Size.MEDIUM: self.pizza.price_medium * self.quantity,
            Size.LARGE: self.pizza.price_large * self.quantity,
        }
        return pizza_price_size_mapping[self.size]
