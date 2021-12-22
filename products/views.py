from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from products.models import Product


def product_list(request: HttpRequest):
    product_list = Product.objects.order_by('-id')
    return render(request, "products/product_list.html", {
        "product_list": product_list
    })


def product_detail(request: HttpRequest, id):
    product = get_object_or_404(Product, id=id)

    return render(request, "products/product_detail.html", {
        "product": product
    })
