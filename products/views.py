from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from qna.models import Question


def product_list(request: HttpRequest):
    products = Product.objects.order_by('-id')
    return render(request, "products/product_list.html", {
        "products": products
    })


def product_detail(request: HttpRequest, id):
    product = get_object_or_404(Product, id=id)

    product_reals = product.product_reals.order_by('option_1_display_name', 'option_2_display_name')

    return render(request, "products/product_detail.html", {
        "product": product,
        "product_reals": product_reals
    })


def question_create(request: HttpRequest, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        product_content_type = ContentType.objects.get_for_model(product)
        body = request.POST.get("body")
        question = Question(user_id=1, content_type=product_content_type, object_id=product.id, body=body)
        question.save()

        messages.success(request, "질문이 등록되었습니다.")

        return redirect("products:detail", id=product.id)

    product_reals = product.product_reals.order_by('option_1_display_name', 'option_2_display_name')

    return render(request, "products/product_detail.html", {
        "product": product,
        "product_reals": product_reals
    })
