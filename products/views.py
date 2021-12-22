from django.shortcuts import render

from django.http import HttpRequest, HttpResponse


def product_list(request:HttpRequest):
    return HttpResponse("Hi")