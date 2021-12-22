from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from products.models import Product


def product_list(request:HttpRequest):
    product_list = Product.objects.order_by('-id')

    return render(request, "products/product_list.html", {
        "product_list": product_list
    })