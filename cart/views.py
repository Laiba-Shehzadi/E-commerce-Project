from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem
from store.models import Product
from .models import CartItem, Order, OrderItem

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if not request.user.is_authenticated:
        return redirect('login')

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('product_list')


def cart_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    cart_items = CartItem.objects.filter(user=request.user)

    total = sum(item.total_price for item in cart_items)

    return render(request, "cart/cart.html", {
        "cart_items": cart_items,
        "total": total,
    })


def remove_from_cart(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')

    item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    item.delete()

    return redirect('cart')


def increase_quantity(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')

    item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    item.quantity += 1
    item.save()

    return redirect('cart')


def decrease_quantity(request, item_id):
    if not request.user.is_authenticated:
        return redirect('login')

    item = get_object_or_404(
        CartItem,
        id=item_id,
        user=request.user
    )

    if item.quantity > 1:
        item.quantity -= 1
        item.save()
    else:
        item.delete()

    return redirect('cart')
def checkout(request):

    cart_items = CartItem.objects.filter(user=request.user)

    total = sum(item.total_price for item in cart_items)

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        city = request.POST.get("city")

        order = Order.objects.create(
            user=request.user,
            name=name,
            email=email,
            phone=phone,
            address=address,
            city=city,
            total=total
        )

        for item in cart_items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        cart_items.delete()

        return render(
            request,
            "cart/order_success.html",
            {
                "order": order
            }
        )

    return render(
        request,
        "cart/checkout.html",
        {
            "cart_items": cart_items,
            "total": total
        }
    )
def my_orders(request):
    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    return render(
        request,
        "cart/my_orders.html",
        {
            "orders": orders
        }
    )
def order_detail(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(request, "cart/order_detail.html", {
        "order": order
    })
