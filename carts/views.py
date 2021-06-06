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
    total_price=0
    tax = 0
    grand_total = 0
    cart = Cart.objects.get(cart_id = _cart_id(request))
    cart_items = CartItem.objects.filter(cart = cart)
    for cart_item in cart_items:
        total_price += cart_item.course.price * cart_item.quantity
        tax = round(0.2*total_price,2)
        grand_total = total_price + tax
    context = {
        'cart_items' : cart_items,
        'total_price' : total_price,
        'tax' : tax,
        'grand_total' : grand_total
    }
    return render(request, 'store/carts.html', context)
    
def remove_cart(request, course_id):
    course = Course.objects.get(id=course_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.get(course = course, cart = cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

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

def remove(request, course_id):
    course = Course.objects.get(id=course_id)
    cart = Cart.objects.get(cart_id=_cart_id(request))
    cart_item = CartItem.objects.filter(cart=cart, course=course)
    cart_item.delete()
    return redirect('cart')