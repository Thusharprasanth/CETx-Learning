from carts.models import Cart, CartItem
from django.shortcuts import redirect, render
from courses.models import Course

# Create your views here.
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def cart(request):
    cart = Cart.objects.get(cart_id = _cart_id(request))
    cart_items = CartItem.objects.filter(cart = cart)
    context = {
        'cart_items' : cart_items
    }
    return render(request, 'store/carts.html', context)

def add_cart(request, course_id):
    course = Course.objects.get(id=course_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(course=course, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            course = course,
            quantity =1 ,
            cart= cart,
        )
    cart_item.save()
    
    return redirect('cart')