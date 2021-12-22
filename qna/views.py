from django.http import HttpRequest
from django.shortcuts import render

def create_question(request:HttpRequest):
    return HttpRequest("hi")
