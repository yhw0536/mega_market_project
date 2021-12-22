from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from products.models import Product


def product_list(request: HttpRequest):
    product_list = Product.objects.order_by('-id')
    return render(request, "products/product_list.html", {
        "product_list": product_list
    })


def product_detail(request: HttpRequest, id):
    return HttpResponse(f"상품 상세페이지, {id}")
