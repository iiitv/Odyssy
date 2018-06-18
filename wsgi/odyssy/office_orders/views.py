from django.shortcuts import render
from office_orders.models import OfficeOrders


def view_office_orders(request):
    orders = OfficeOrders.get_all_active_orders()
    context = {
        'orders': orders
        }
    return render(request, 'office_orders/order.html', context=context)


def view_archive(request):
    orders = OfficeOrders.get_archives()
    context = {
        'orders': orders
    }
    return render(request, 'office_orders/archive.html', context=context)
