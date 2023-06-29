from .models import Category, CartProduct, Cart

def category(request):
    category = Category.objects.all()
    context = {
        'categorys': category
    }
    return context

# def catproducts(request):
    cart_id = request.session.get('cart_id',None)
    if cart_id:
        cart_item = Cart.objects.get(id = cart_id)
         # check or assign cart to a registered user
        if request.user.is_authenticated and request.user.profile:
            cart_item.profile = request.user.profile
            cart_item.save()
        cart_products = cart_item.cartproduct_set.all()
        num_of_product = cart_products.count()
    else:
        cart_item = None

    # context = {
    #     'items' : num_of_product
    # }

    return context
    # pass