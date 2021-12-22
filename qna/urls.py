from django.urls import path
from qna import views

app_name = 'qna'

urlpatterns=[
    path('create_question', views.create_question, name='create_question')
]