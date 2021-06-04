from courses.models import Course
from django.db import models
from courses.models import Course

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=30)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.course