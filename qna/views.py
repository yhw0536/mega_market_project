from django.contrib.contenttypes.models import ContentType
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from products.models import Product
from qna.models import Question


def create_question(request: HttpRequest):
    product_id = 1
    product = Product.objects.get(id=product_id)
    product_content_type = ContentType.objects.get_for_model(product)
    body = request.POST.get("body")
    question = Question(user_id=1, content_type=product_content_type, object_id=product_id, body=body)
    question.save()
    return HttpResponse("성공")