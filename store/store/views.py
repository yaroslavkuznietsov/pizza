from django.shortcuts import render
from store.models import Pizza
from store.forms import PizzaForm
from store.models import OrderItem
from store.models import Order


# Create your views here.


def index(request):
    print(request.POST)

    if request.method == 'POST':
        query_dict_to_dict(request.POST)

    items = Pizza.objects.all()
    return render(request, 'store/index.html', {'items': items, 'form': PizzaForm})


def query_dict_to_dict(query_dict):
    """
    get all values from query dictionary
    :param query_dict:
    :return:
    """

    temp_dict = query_dict.dict()
    # print(temp_dict)
    # print(f" pizza: {temp_dict.get('pizza')}")
    # print(f" quantity: {temp_dict.get('quantity')}")
    # print(f" size: {temp_dict.get('size')}")

    temp_order = Order()
    temp_order.address = temp_dict.get('address')
    temp_order.phone = temp_dict.get('phone')
    temp_order.comments = temp_dict.get('comments')
    temp_order.save()
    # Order.objects.create(address=temp_order.address, phone=temp_order.phone, comments=temp_order.comments)

    order_item = OrderItem()
    order_item.pizza = Pizza.objects.get(id=temp_dict.get('pizza'))

    order_item.order = temp_order

    order_item.quantity = temp_dict.get('quantity')
    order_item.size = temp_dict.get('size')


    OrderItem.objects.create(pizza=order_item.pizza, quantity=order_item.quantity, order=temp_order, size=order_item.size)

    print(order_item)
    return order_item
