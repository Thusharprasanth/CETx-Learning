from .models import CartItem, Cart
from .views import _cart_id
def cart_counter(request):
    cart_count = 0
    cart = Cart.objects.filter(cart_id = _cart_id(request))
    cart_items = CartItem.objects.all().filter(cart = cart[:1])
    for cart_item in cart_items:
        cart_count += cart_item.quantity
    return dict(cart_count=cart_count)